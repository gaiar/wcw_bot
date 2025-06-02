#!/usr/bin/env bash

# YOLOv4 works better with OpenCV 4.5.2
wget https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4.weights
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names -O yolov4.txt

# Fallback to YOLOv3 if needed (kept for reference)
# wget https://pjreddie.com/media/files/yolov3.weights
# wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
# wget https://raw.githubusercontent.com/arunponnusamy/object-detection-opencv/master/yolov3.txt
