# Image-Upscale
running the image upscale for the various upscaling algorithms

## See the Link , See the community more
[Upscale Community](https://openmodeldb.info/)
不同场景下的增强画质模型，支持不同的商业用途！

## download models
一些模型的size 比较大，上传会显示失败！在部署前的预处理先下载这些模型，并存放指定路径。

**人脸超分模型：**

[RestoreFormer.pth](https://github.com/wzhouxiff/RestoreFormer) 

**检测人脸模型：**

detection_Resnet50_Final.pth 

parsing_parsenet.pth

## Dir Construct

```code
Image-Upscale/
|
|-- assets/                         # Directory to store assets
|-- bin/                            # Directory for image-upscale executor
|-- master/                         # Directory for main processors
|   |-- figure                      # Preprocessing functions and utilities
|   |-- |-- figureInference.py      # Figure model processing scripts 
|   |-- gfpgan                      # Detect figure basic model
|   |-- |-- weights
|   |-- |-- |-- detection_Resnet50_Final.pth # Detect protrait 
|   |-- |-- |-- parsing_parsenet.pth         # Parsing protrait
|   |-- constants.py                # File contains all default constants
|   |-- instance.py                 # Input args test file
|   |-- logsConfig.py               # Logs config file
|   |-- main.py                     # main file
|
|-- models/                         # Directory for saving all models
|
|-- output/                         # Directory for output image file
|-- .gitignore                      # not uploaded file or dir
|-- LICENSE                         # MIT LICENSE
|-- README.md                       # Project documentation and instructions
|-- requirements.txt                # List of dependencies and required libraries

```

## LOGGING MODULE

master/constants.py的 DEBUG_MODE 决定日志是否开启debug模式

## Citation

@article{wang2022restoreformer,
  title={RestoreFormer: High-Quality Blind Face Restoration from Undegraded Key-Value Pairs},
  author={Wang, Zhouxia and Zhang, Jiawei and Chen, Runjian and Wang, Wenping and Luo, Ping},
  booktitle={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2022}
}

