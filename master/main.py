from subprocess import check_call

from constants import *
from instance import *


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
    
def main():
    
    # instants实例
    # commands args参数组合
    arguments = getSingleImageArguments(inputDir,fullfileName,outFile,modelsPath,model,scale,gpuid,saveImageAs)
    check_call(spawnUpscaling(COMMANDS,arguments))
    return


if __name__ == '__main__' :
    main()
    
    