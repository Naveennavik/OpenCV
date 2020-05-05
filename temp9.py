# Implementation of different tracking APIs

import cv2
import numpy as np

cap = cv2.VideoCapture('/home/drive/Downloads/zav2/VIBE/process_imgs/zzz/KGbowls.mp4')

#Set up intitial location for tracking:
ret, frame = cap.read()

H, W = frame.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('/home/drive/Downloads/zav2/VIBE/process_imgs/zzz/out/KGbowls.mp4', fourcc, 25, (W,H))

# print(H, W)   

# nh = int(H * 25//100)
# nw = int(W * 25//100)

# tempFrame = cv2.resize(frame, (nw,nh))

# tcpy = tempFrame.copy()
flag = 1

while True:
    # Read a new frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Display tracker type on frame
    cv2.putText(frame, "3D Body Structure", (70,70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2);
 
    # Display result
    cv2.imshow("Tracking", frame)
    out.write(frame)
    
    # Exit if ESC pressed
    k = cv2.waitKey(25) & 0xff
    if k == 27 : 
    	break


cap.release()
cv2.destroyAllWindows()
out.release()

#blackd = np.zeros(frame.shape, np.uint8)
#blackd[p1[1]:p2[1], p1[0]:p2[0]] = frame[p1[1]:p2[1], p1[0]:p2[0]]
#cv2.imshow("Onblack", blackd)

