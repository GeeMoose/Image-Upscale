import os
import cv2
# import gradio as gr
import torch
from basicsr.archs.srvgg_arch import SRVGGNetCompact
from basicsr.archs.rrdbnet_arch import RRDBNet
from gfpgan.utils import GFPGANer
from realesrgan.utils import RealESRGANer

# 增强背景可使用RealESRGAN_x2plus.pth模型
def set_realesrgan(model,model_path):
    half=True if torch.cuda.is_available() else False
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
    return RealESRGANer(scale=2, model_path=model_path +'/' + "RealESRGAN_x2plus.pth", model=model, tile=400, tile_pad=10, pre_pad=0, half=half)

def set_figure_face_enhancer(upsampler, model, model_path):
    return GFPGANer(model_path=model_path +'/' + model, upscale=2, arch='clean', channel_multiplier=2, bg_upsampler=upsampler)

def figure_inference(input_img, outFile, scale, model_path, model, gpuid, saveImageAs):
    # 根据已有的模型做输出
    scale = int(scale)
    if scale > 4:
        scale = 4
    elif scale < 0:
        scale = 1
    
    scale = int(scale)
    
    try:
        # img_name = os.path.splitext(os.path.basename(str(input_img)))[0]
        img = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
        if len(img.shape) == 3 and img.shape[2] == 4:
            img_mode = 'RGBA'
        elif len(img.shape) == 2:  # for gray inputs
            img_mode = None
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        else:
            img_mode = None

        h, w = img.shape[0:2]
        if h > 3500 or w > 3500:
            print('too large size')
            return None, None
        
        if h < 300:
            img = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_LANCZOS4)

        upsampler = set_realesrgan(model, model_path)
        face_enhancer = set_figure_face_enhancer(upsampler, model, model_path)
        
        try:
            _, _, output = face_enhancer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True, weight=None)
        except RuntimeError as error:
            print('Error', error)

        try:
            if scale != 2:
                interpolation = cv2.INTER_AREA if scale < 2 else cv2.INTER_LANCZOS4
                h, w = img.shape[0:2]
                output = cv2.resize(output, (int(w * scale / 2), int(h * scale / 2)), interpolation=interpolation)
        except Exception as error:
            print('wrong scale input.', error)
        if img_mode == 'RGBA':  # RGBA images should be saved in png format
            saveImageAs = 'png'
        else:
            saveImageAs = 'jpg'
        # save_path = f'../../output/{img_name}_out.{saveImageAs}'
        cv2.imwrite(outFile, output)

        output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        return output, outFile
    
    except Exception as error:
        return None, None
 

        