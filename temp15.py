import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

filename = "7140a911-afe4-4963-9a1d-e444587cf814-7140a911-afe4-4963-9a1d-e444587cf814.mp4"
cap = cv2.VideoCapture('/home/drive/Downloads/zav2/mlb data feb17/trim/' + filename)

ret, frame = cap.read()

flag = 0

bbox = cv2.selectROI(frame, False)
x, y, w, h = bbox
##bbxo -> (x,y,w,h)
## b525 - (444, 129, 340, 494)
## e52c - (421, 108, 359, 513)
## 7140 - (416, 120, 369, 536)

print(x, y, w, h)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('/home/drive/Downloads/zav2/mlb data feb17/7140out.mp4',fourcc, 60, (w,h))

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break

    
    #print(frame[y:y+h,x:x+w].shape)
    fr = frame[y:y+h,x:x+w]
    out.write(fr)
    cv2.imshow('img',fr)

    # Exit if ESC pressed
    k = cv2.waitKey(20) & 0xff
    if k == 27 : 
    	break

cap.release()
cv2.destroyAllWindows()