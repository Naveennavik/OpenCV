import cv2
import numpy as np 
import matplotlib.pyplot as plt

# Trim the video as needed:
import moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#ffmpeg_extract_subclip("/home/drive/Downloads/tennishl.mp4", 180, 358, targetname="/home/drive/Downloads/tvideo3.mp4")

cap = cv2.VideoCapture('/home/drive/Downloads/tvideo2.mp4')


ret, prev = cap.read()

w, h = prev.shape[1], prev.shape[0]

#four_cc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('/home/drive/Downloads/extract2.mp4', four_cc, 25.0, (w,h))

fgbg = cv2.createBackgroundSubtractorMOG2()



if not cap.isOpened():
	print("Video open failed")
	exit()

while cap.isOpened():

	img_bg = cv2.imread('/home/drive/Downloads/res.jpg')

	#capture it frame by frame
	ret, frame = cap.read()  #ret-> boolean that says if the video has been read

	if not ret:
		print("End of frames...")
		break

	target = frame.copy()

	mask = np.zeros(target.shape[0:2], np.uint8)
	mask2 = np.zeros(target.shape[0:2], np.uint8)
	mask3 = np.zeros(target.shape[0:2], np.uint8)

	mask2[200:573, 162:1098] = 255

	gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 50, 150, apertureSize=3)
	dilated = cv2.dilate(edges, np.ones((2,2), dtype=np.uint8))
	imag, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	#print(len(contours))

	cnt = sorted(contours, key = cv2.contourArea, reverse = True)[0]
	area = cv2.contourArea(cnt)
	
	if area > 150000.0:

		epsilon = 0.001*cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)	
		#print(approx[1][0])  #### Approx has the 4 coordinates ####

		# Draw the contours on a black image
		
		mask3 = cv2.merge((mask3,mask3,mask3))
		cv2.drawContours(mask3,[approx],-1,(0,255,0),2)
		mask3 = cv2.bitwise_and(mask3, mask3, mask=mask2)
		

		cv2.drawContours(mask,[approx],-1,255,-1)
		mask = cv2.bitwise_and(mask, mask2)
		mask = cv2.merge((mask,mask,mask))
		res = cv2.bitwise_and(target, mask)

	else:

		# x = int(mask.shape[1]/2)
		# y = int(mask.shape[0]/2)
		#cv2.putText(mask,"Other Camera", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 4)
		mask = cv2.merge((mask,mask,mask))
		res = mask


	fgmask = fgbg.apply(res)

	#er = cv2.erode(fgmask, np.ones((5,5),np.uint8))
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	#op = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	#cl = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	op = cv2.dilate(fgmask, kernel, iterations=5)

	#fg_gray = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)
	#neg = cv2.bitwise_not(sub)

	res = cv2.bitwise_and(res, res, mask=fgmask)
	#res = cv2.bitwise_and(res, res, mask=op)

	tf = res>0
	#print(tf.shape)

	img_bg[tf] = res[tf]

	#cv2.imshow("FGBG", fgmask)
	cv2.imshow("Dilatedx",res)
	cv2.imshow("Final",img_bg)
	
	

	#result = histogramBP(target, roi)

	#out.write(res)

	#cv2.imshow("Original", frame)
	# cv2.imshow("Original", frame)
	# cv2.imshow("Final", res)
	#cv2.imshow('Final', result)


	#Press Q on keyboard to quit
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

#Release the capture
cap.release()
#out.release()
cv2.destroyAllWindows()