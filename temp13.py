import pandas as pd
import numpy as np
import cv2
import ast

#o/p of /home/drive/openpose_tuple_csv.ipynb#
df = pd.read_csv("/home/drive/Downloads/tup_pts.csv")
cap = cv2.VideoCapture("/home/drive/Downloads/zav2/openpose/output/cricket_sample_outputs/cricket_sample_21pts.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/drive/Downloads/cricket_sample_2d_21.mp4',fourcc, 60, (480,848))

count = 0

pairs = [['1','2'],['2','3'], ['3','4'], ['1','5'], ['5', '6'], ['6','7'], ['1', '8'],
		['8','9'], ['9','10'], ['10','11'], ['8','12'], ['12','13'], ['13','14'], ['15','17'],
		['16','18'], ['15','0'], ['0','16'], ['0','19'], ['19','1'], ['0','20']]
		
for i in range(df.shape[0]):
	img = np.zeros([848, 480, 3], dtype=np.uint8)
	#ret, img = cap.read()
	#if not ret:
		#break
	
	for pair in pairs:
		a = ast.literal_eval(df.loc[i,pair][0])
		b = ast.literal_eval(df.loc[i,pair][1])
		if a == (0,0) or b == (0,0):
			continue
		img = cv2.line(img, a, b, (255,105,105), 2)

	coords = df.loc[i].to_list()[1:]
	for coord in coords:
		co = ast.literal_eval(coord)
		if co == (0,0):
			continue
		cv2.circle(img, co, 4, (78,241,166), -1)
		#print(coord)

	out.write(img)

	cv2.imshow('img', img)
	k = cv2.waitKey(20)

	if k & 0xFF == 27:
		break
	count += 1

out.release()
cap.release()
cv2.destroyAllWindows()
print(count)