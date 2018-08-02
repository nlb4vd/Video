# Video

## Introduction
With this repo, you will be able to crop, stabilize, and run image-recognition on videos.

## Downloads needed
1. You will need ffmpeg downloaded, available from https://ffmpeg.org/download.html. If you are on windows, you will just need ffmpeg.exe, which is already in the repo.

2. You will need Ffmpeg-python, which can be downloaded with pip:
```
pip install ffmpeg-python
```
The full documentation for ffmpeg-python can be found here: https://github.com/kkroening/ffmpeg-python

3. You will need vidstab, which can also be installed with pip. If you alerady have opencv installed, then you can use:
```
pip install vidstab
```
If you don't have opencv installed already, you can use:
```
pip install vidstab[cv2]
```
The full documentation for vidstab can be found here:  https://github.com/AdamSpannbauer/python_video_stab

4. Yolov3, the object detector, is implimented via pytorch and is already included in the repo. The full documentation can be found here: https://github.com/ayooshkathuria/pytorch-yolo-v3

##Running
###Cropping and Stabilizing
