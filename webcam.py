import cv2
from PIL import Image
import frame as fr

cv2.namedWindow("blindEye preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("blindEye preview", frame)
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(frame)
    print("Distance = " + str(fr.getTotalDistance(im_pil)))
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("blindEye preview")
