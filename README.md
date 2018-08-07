# Video

## Introduction
With this repo, you will be able to crop, stabilize, compress, clip, and run image-recognition on videos.

## Downloads needed
### Ffmpeg
Ffmpeg is available from https://ffmpeg.org/download.html. 

### Ffmpeg-python
Ffmpeg-python can be downloaded with pip:
```
pip install ffmpeg-python
```
The full documentation for ffmpeg-python can be found here: https://github.com/kkroening/ffmpeg-python

### Vidstab
Vidstab can be installed with pip. If you already have opencv installed, then you can use:
```
pip install vidstab
```
If you don't have opencv installed already, you can use:
```
pip install vidstab[cv2]
```
The full documentation for vidstab can be found here:  https://github.com/AdamSpannbauer/python_video_stab

### Pytorch-Yolov3
Yolov3, the object detector, is implemented via pytorch and is already included in the repo. The only thing that needs to be downlaoded for this (and put into the yolov3 folder) is the weights file, which can be downloadd here: https://pjreddie.com/media/files/yolov3.weights


The full documentation can be found here: https://github.com/ayooshkathuria/pytorch-yolo-v3

## Running
### Cropping and Stabilizing
**IMPORTANT NOTE: Stabilization only seems to work when the cropped video file is an mp4 and the stabilized video file is an avi**

To crop and stabilize files, run crop-and-stab.py like so:
```
python crop-and-stab.py --video inputVideo.avi --outcrop croppedVideo.mp4 --outstab stabbedVideo.avi
```
The --video flag is the inputted video, the --outcrop flag is the name of the cropped file, and the --outstab flag is the name of the cropped and stabilized video.

### Compressing
**IMPORTANT NOTE: Smile only runs avi files, so make sure these videos are outputted as an avi**

To compress a file, run compress.py:
```
python compress.py --video inputVideo.avi --outvid outputVideo.avi
```
The --video flag is the inputted video and the --ouvid flag is the outputted video.

### Cropping, Stabilizing, and Compressing Folders

To crop, stabilize, and compress entire folders of movies, run folder.py:
```
python folder.py --input INPUT, --output OUTPUT, --stab False, --deleteInter True
```
The --input flag is the input directory, the --output flag is the output directory, the --stab flag is whether or not you would like to run image stabilization, and the --deleteInter flag is whether or not you would like to delete the intermediate files (recommended)

Note: the format for the input and output files, currently, should be the name of the folder (in the current directory) without a "/" in front of it

### Clipping Videos

To clip video files, run clip.py:
```
python clip.py --input inputVideo.avi --output outputVideo.avi --start 60 --end 65
```
The --input flag is the input video, the --output flag is the output video, the --start flag is the start time in seconds, and the --end flag is the end time in seconds

### Object Recognition
To run object recognition, cd to the pytorch-yolo-v3 folder and run object-rec.py:
```
python object-rec.py --video inputVideo.avi --outtext outText.txt
```
The --video flag is the input video and the --outtext flag is the output text. Other options exist for the image recognition, use the -h flag for more options.


