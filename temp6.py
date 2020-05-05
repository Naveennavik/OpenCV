import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

tracker_ids = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
#tracker_ids = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_types = []

rand = random.randint(0,6)

tracker_type = tracker_ids[6]

if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
# elif tracker_type == 'GOTURN':
#     tracker = cv2.TrackerGOTURN_create()
elif tracker_type == 'MOSSE':
    tracker = cv2.TrackerMOSSE_create()
else:
    tracker = cv2.TrackerCSRT_create()

cap = cv2.VideoCapture('/home/drive/Downloads/golfswing2.mp4')

#Set up intitial location for tracking:

ret, frame = cap.read()

H, W = frame.shape[:2]

# print(H, W)

# nh = int(H * 25//100)
# nw = int(W * 25//100)

# tempFrame = cv2.resize(frame, (nw,nh))

# tcpy = tempFrame.copy()
flag = 0

bbox = cv2.selectROI(frame, False)

b, g, r = cv2.split(frame)

ret, thresh = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('/home/drive/Downloads/Sport/videogg.avi',fourcc, 25, (1280,720))


# new_bbox = find_bbox(bbox, nw, nh)


t = tracker.init(thresh, bbox)

while True:
        # Read a new frame
        ret, frame = cap.read()
        if not ret:
            break

        #tempFrame = cv2.resize(frame, (nw,nh))

        b, g, r = cv2.split(frame)

        ret, thresh = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(g)
 
        # Update tracker
        ok, bbox = tracker.update(thresh)
 
        # Draw bounding box
        if ok:


            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

            x = int(bbox[0]+bbox[2]/2)
            y = int(bbox[1]+bbox[3]/2)

        
           
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            #cv2.rectangle(thresh, p1, p2, 255, 2, 1)
            
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        
        # Display result
        cv2.imshow("Tracking", frame)
        cv2.imshow("Threshold", thresh)

        tg = cv2.merge((cl1,cl1,cl1))
        out.write(tg)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
        	break

cap.release()
cv2.destroyAllWindows()