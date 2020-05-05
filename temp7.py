import cv2
import numpy as np
import pandas as pd
import ast

cap = cv2.VideoCapture("/home/drive/Downloads/Sport/video2x2.avi")

ret, frame = cap.read()

h,w = frame.shape[:2]

frame_number = 1
count = 0

data = pd.read_csv("/home/drive/Downloads/sub71.csv")
centerList = []
frameList = []
for i in range(data.shape[0]):
    temp = ast.literal_eval(data['center'][i])
    centerList.append(temp)
    frameList.append(data["frame_number"][i])

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/drive/Downloads/Sport/videoOut9.avi',fourcc, 30, (w,h))

while cap.isOpened():

	ret, frame = cap.read()
	frame_number += 1

	if not ret:
		break

	if frame_number >= 58:
		#print(count)

		# if frame_number == 33:
		# 	cv2.circle(frame, centerList[0], 8, (0,165,240),-1)
		for i in range(0, count):
			cv2.circle(frame, centerList[i], 5, (0,165,240),-1)
			#cv2.line(frame, centerList[i-1], centerList[i], (0,165,240), 8)

		if frame_number in frameList:
			count += 1

	cv2.imshow("Out", frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

	if frame_number <= 120:
		out.write(frame)

	

cap.release()
#out.release()
cv2.destroyAllWindows()

