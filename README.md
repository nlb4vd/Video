# Video

## Introduction
With this repo, you will be able to crop, stabilize, and run image-recognition on videos.

## Downloads needed
### Ffmpeg
Ffmpeg available from https://ffmpeg.org/download.html. If you are on windows, you will just need ffmpeg.exe, which is already in the repo.

### Ffmpeg-python
Ffmpeg-python can be downloaded with pip:
```
pip install ffmpeg-python
```
The full documentation for ffmpeg-python can be found here: https://github.com/kkroening/ffmpeg-python

### Vidstab
Vidstab can be installed with pip. If you alerady have opencv installed, then you can use:
```
pip install vidstab
```
If you don't have opencv installed already, you can use:
```
pip install vidstab[cv2]
```
The full documentation for vidstab can be found here:  https://github.com/AdamSpannbauer/python_video_stab

### Pytorch-Yolov3
Yolov3, the object detector, is implimented via pytorch and is already included in the repo. The full documentation can be found here: https://github.com/ayooshkathuria/pytorch-yolo-v3

## Running
### Cropping and Stabilizing
**IMPORTANT NOTE: At least on my machine, stabilization only seems to work when the cropped video file is an mp4 and the stabilized video file is an avi**

To crop and stabilize files, run crop-and-stab.py like so:
```
python crop-and-stab.py --video inputVideo.avi --outcrop croppedVideo.mp4 --outstab stabbedVideo.avi
```
The --video flag is the inputted video, the --outcrop flag is the name of the cropped file, and the --outstab flag is the name of the cropped and stabilized video.

### Compressing
**IMPORTANT NOTE: I believe that Smile only runs avi files, so make sure these videos are outputted as an avi**

To compress a file, run compress.py:
```
python compress.py --video inputVideo.avi --outvid outputVideo.avi
```
The --video flag is the inputted video and the --ouvid flag is the outputted video.

### Object Recognition
To run object recognition, cd to the pytorch-yolo-v3 folder and run object-rec.py:
```
python object-rec.py --video inputVideo.avi --outtext outText.txt
```
The --video flag is the input video and the --outtext flag is the output text. Other options exist for the image recognition, use the -h flag for more options.
