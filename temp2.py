import cv2
import numpy as np
import sys

def nothing(x):
    pass

# cap = cv2.VideoCapture('/media/drive/C47409FF7409F548/SwingU_Videos/SwingU_1.mp4')
cap = cv2.VideoCapture('/home/drive/Downloads/Golf1.mp4')



# cv2.namedWindow("Tracking")
# cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
# cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
# cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
# backSub = cv2.createBackgroundSubtractorMOG2()

if not cap.isOpened():
    print("Could not open video")
    sys.exit()

# Read first frame
ok,frame = cap.read()

if not ok:
    print("Cannot read video file")
    sys.exit()

tracker = cv2.TrackerCSRT_create()
# tracker = cv2.Tracker_create('CSRT')
h1,w1,ch = frame.shape

nh = int(h1*(200/100))
print(nh)
nw = int(w1*(200/100))
print(nw)

frame = cv2.resize(frame,(nw,nh),interpolation = cv2.INTER_AREA)
bbox = cv2.selectROI(frame, False)

#-----------------------------------------#
b, g, r = cv2.split(frame)
h, w = g.shape
# g2 = g[int(h/2):, :]
g2 = g
ret,thresh1 = cv2.threshold(g2,200,255,cv2.THRESH_BINARY)
# thresh1 = cv2.adaptiveThreshold(g2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

kernel = np.ones((3,3),np.uint8)
thresh1 = cv2.erode(thresh1,kernel,iterations = 1)
kernel2 = np.ones((5,5),np.uint8)
thresh1 = cv2.dilate(thresh1,kernel2,iterations = 1)
#------------------------------------------#

ini_fr = np.zeros((h,w),dtype='uint8')
ini_fr[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]] = thresh1[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]]
cv2.imshow('initial_frame', ini_fr)
cv2.waitKey(0)
ok = tracker.init(ini_fr, bbox)

#---------------------------------------------------------------------------#
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('SwingU_Tracking_Plot_1.mp4',fourcc, 240.0, (nw,nh))
centers = []
count = 0
while(cap.isOpened()):
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()

    if frame is None:
	    print("BYE")
	    break

    frame = cv2.resize(frame,(nw,nh),interpolation = cv2.INTER_AREA)
#---------------------------------------------------#
    b, g, r = cv2.split(frame)
    # h, w = g.shape
    # g2 = g[int(h/2):, :]
    g2 = g
    ret,thresh1 = cv2.threshold(g2,200,255,cv2.THRESH_BINARY)
    # thresh1 = cv2.adaptiveThreshold(g2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    kernel = np.ones((3,3),np.uint8)
    thresh1 = cv2.erode(thresh1,kernel,iterations = 1)
    kernel2 = np.ones((5,5),np.uint8)
    thresh1 = cv2.dilate(thresh1,kernel2,iterations = 1)
    # thresh1 = backSub.apply(thresh1)
#---------------------------------------------------#
    timer = cv2.getTickCount()

        # Update tracker
    ok, bbox = tracker.update(thresh1)

        # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        if count>520 and count<600:

            x = int(bbox[0]+bbox[2]/2)
            y = int(bbox[1]+bbox[3]/2)
            centers.append((x,y))
        count = count+1

            # p1 = (xx, yy)
            # p2 = (xx+ww, yy+hh)

        for center in centers:
            cv2.circle(frame, center, 5, (0 ,0 ,255), -1)
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)


    # Display result
    cv2.imshow("Tracking", frame)
    

    key = cv2.waitKey(1)
    if key == 27:
        break

# out.release()
cap.release()
cv2.destroyAllWindows()

print('before',centers)
centers.sort()
print('After',centers)

x = np.array([xc[0] for xc in centers])

y = np.array([xc[1] for xc in centers])



import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt

# x = np.array([349. , 349., 349., 349.])
# y = np.array([742. , 743., 743., 742.])

t, c, k = interpolate.splrep(x, y, s=0)

print('''\
t: {}
c: {}
k: {}
'''.format(t, c, k))
N = 100
xmin, xmax = x.min(), x.max()
xx = np.linspace(xmin, xmax, N)
spline = interpolate.BSpline(t, c, k, extrapolate=True)

plt.plot(x, y, 'bo', label='Original points')
plt.plot(xx, spline(xx), 'r', label='BSpline')
plt.grid()
plt.legend(loc='best')
plt.show()