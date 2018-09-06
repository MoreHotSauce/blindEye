import sys
from yolo import YOLO, detect_video
from PIL import Image
import numpy as np
import cv2

iYolo = YOLO()

#get middle of the first found stop sign
def middle(boxes, output):
    if len(output) == 0:
        return (False, False)
    signIndex = np.where(output==11)
    return [((boxes[signIndex][0][0] + boxes[signIndex][0][2]) / 2), ((boxes[signIndex][0][1] + boxes[signIndex][0][3]) / 2)]
#distance formula
def distance(x1, y1, x2, y2):
    return np.sqrt(np.square(x2-x1) + np.square(y2-y1))
#get total distance
def getTotalDistance(image):
    image = image.resize((100, 100))
    boxes, labels = iYolo.detect_image(image)
    y, x = middle(boxes, labels)
    if not y:
      return 50
    return distance(50, 50, x, y)
