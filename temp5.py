import numpy as np
import cv2

cap = cv2.VideoCapture("/home/drive/Downloads/vknet.mp4")

for i in range(300):
	ret, frame = cap.read()

h, w = frame.shape[:2]
#print(h, w)

bbox = cv2.selectROI("First", frame)

nh = bbox[1] + bbox[3]
nw = bbox[0] + bbox[2]

final = np.zeros((nh, nw, 3), np.uint8)
print(nw, nh)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/drive/Downloads/vk2net.mp4',fourcc, 30, (bbox[2], bbox[3]))

count = 0
while cap.isOpened():

	ret, frame = cap.read()
	count += 1

	if not ret:
		print("End of frames...")
		break

	final = frame[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
	
	if (count % 600 == 0):
		print(final.shape)
		
	cv2.imshow("final", final)
	out.write(final)

	if cv2.waitKey(1) & 0xFF == 27:
		break

out.release()
cv2.destroyAllWindows()
cap.release()