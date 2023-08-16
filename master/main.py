from flask import Flask
from flask import request
from flask import send_file, jsonify

from  flask_cors import CORS

from subprocess import check_call
from PIL import Image

from constants import *
from instance import *

import os, base64

app = Flask(__name__)
CORS(app)

# 批处理超分
def folder_upscale_image():
    return 

# 双倍超分
def double_upscale_image():
    return 

# 超分
def upscale_image():
    return 

def getSingleImageArguments(inputDir,fullfileName,outFile,modelsPath,model,scale,gpuid,saveImageAs):
    return [
    "-i",
    inputDir + SLASH + fullfileName,
    "-o",
    outFile,
    "-s",
    scale,
    "-m",
    modelsPath,
    "-n",
    model,
    "-g",
    gpuid,
    "-f",
    saveImageAs,
  ]

def spawnUpscaling(commands,arguments):
    args = ','.join([arg for arg in arguments])
    executor = commands + ',' + args
    return executor.split(',')

@app.route('/')
def index():
    return "Editing Image Test"

@app.route('/image-upscaling', methods=['GET','POST'])
def imageUpscaling():
    if request.method == 'GET':
        return "Upscaling Image Test"
    if request.method == 'POST':
        # 如果ImageFile上传文件不符合规范
        print(request.files.get('ImageFile') )
        if request.files.get('ImageFile')  == None:
            return jsonify({'errors': 'ImageFile does not meet specifications'})
        file_obj = request.files['ImageFile']
        if file_obj != None and file_obj.filename != "":
            fullfileName = file_obj.filename
            file_name,file_ext =  os.path.splitext(fullfileName)
            file_obj.save(inputDir + SLASH + fullfileName)
            imagePath = inputDir + SLASH + file_obj.filename
            model = request.form.get('model')
            imgScale = request.form.get('scale')
            saveImageAs =  file_ext[1:]
            outFile = outputDir + SLASH + file_name + "_upscaling_" + imgScale + "x_" + model + "." + saveImageAs
            arguments = getSingleImageArguments(inputDir,fullfileName,outFile,modelsPath,model,scale,gpuid,saveImageAs)
            check_call(spawnUpscaling(COMMANDS,arguments))
            
            # 2x、3x 缩放
            # e.g. '2' < '3' '3' <  '4'
            if imgScale < scale:
                origin_im = Image.open(imagePath)
                upscale_im = Image.open(outFile)
                new_upscale_im = upscale_im.resize((origin_im.size[0] * int(imgScale), origin_im.size[1] * int(imgScale)))
                new_upscale_im.save(outFile)

            with open(outFile, "rb") as img_file:
                Response = base64.b64encode(img_file.read())
                return Response 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


     
# def main():
    
#     # instants实例
#     # commands args参数组合
#     arguments = getSingleImageArguments(inputDir,fullfileName,outFile,modelsPath,model,scale,gpuid,saveImageAs)
#     check_call(spawnUpscaling(COMMANDS,arguments))
#     return


# if __name__ == '__main__' :
#     main()
    
    