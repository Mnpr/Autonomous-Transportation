import time
import time
import cv2 as cv
import numpy as np

# Import local Modules
from prediction import get_yolo_predictions


# Parameters
CONFIDENCE = 0.5
THRESHOLD_SCORE = 0.5
THRESHOLD_IOU = 0.4

# Model Configuration
CONFIG_PATH = 'yolov4.cfg'
WEIGHT_PATH = 'yolov4.weights'

# Miscellaneous
CUDA = True
WRITE_OUTPUT = False
SHOW_DISPLAY = True

# Input / Output 
INPUT = 'io/sample.mp4'
OUTPUT = 'io/yolo_output.avi'

input = 2 #"./io/sample.mp4"   
    
with open('coco.names', "r", encoding="utf-8" ) as f:
    LABELS = f.read().strip().split("\n")

# Random Labels Color
COLOR = np.random.randint(0, 255, size=(len(LABELS),3), dtype='uint8')

# BBOX , Class Overlay Info
FONT_SCALE = 2
THICKNESS = 2

net = cv.dnn.readNetFromDarknet(CONFIG_PATH, WEIGHT_PATH)

if CUDA: 
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

get_yolo_predictions(
        net,
        INPUT,
        OUTPUT,
        CONFIDENCE,
        THRESHOLD_IOU,
        WRITE_OUTPUT,
        SHOW_DISPLAY,
        LABELS
)