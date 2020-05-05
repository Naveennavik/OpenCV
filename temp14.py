import cv2

cap1 = cv2.VideoCapture("/home/drive/Downloads/zav2/mlb data feb17/trim/e52c9cdd-4dcb-4765-b0a0-a1e20f1f815a-e52c9cdd-4dcb-4765-b0a0-a1e20f1f815a.mp4")

cap2 = cv2.VideoCapture('/home/drive/Downloads/AlphaPose_e52cout.avi')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('/home/drive/Downloads/zav2/mlb data feb17/e52cout_.mp4',fourcc, 60, (1280,720))
x, y, w, h = (421, 108, 358, 512)


while True:
    # Read a new frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 and not ret2:
        break

    
    #print(frame[y:y+h,x:x+w].shape)
    frame1[y:y+h,x:x+w] = frame2
    out.write(frame1)
    cv2.imshow('img',frame1)

    # Exit if ESC pressed
    k = cv2.waitKey(20) & 0xff
    if k == 27 : 
    	break

cap.release()
cv2.destroyAllWindows()

cv2.destroyAllWindows()