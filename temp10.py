'''
Generate MLB stages png

'''

import cv2
import numpy as np

frame1 = cv2.imread("/home/drive/000000/inputs/60/000003_mask.png")

frame2 = cv2.imread("/home/drive/000000/inputs/60/000013_mask.png")

#frame3 = cv2.imread("/home/drive/000000/Inputs_55/000025_imask.png")

frame4 = cv2.imread("/home/drive/000000/inputs/60/000019_mask.png")

frame5 = cv2.imread("/home/drive/000000/inputs/60/000027_mask.png")

h, w = frame1.shape[:2]

res = np.zeros((720, 1280, 3), np.uint8)
print(frame1.shape)
print(frame2.shape)
print(frame4.shape)
print(frame5.shape)

h1 = 200
h2 = h1 + 356

cv2.imshow("f1", frame1[325:325+356, 310:310+256])
print(frame1[325:325+356, 310:310+256].shape)
cv2.waitKey(0)

con = np.hstack((frame1[325:325+356, 310:310+256], frame2[325:325+356, 310:310+256], 
				frame4[325:325+356, 310:310+256], frame5[325:325+356, 310:310+256]))
res[h1:h2, 128:1152] = con

font = cv2.FONT_HERSHEY_DUPLEX 
org = (181, 170)
fontScale = 0.5
color = (255,255,255)
thickness = 1

cv2.putText(res, 'Stage 1: Frame 3', org, font,  
            fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(res, 'Stage 2: Frame 13', (org[0]+256,org[1]), font,  
            fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(res, 'Stage 3: Frame 19', (org[0]+2*256,org[1]), font,  
            fontScale, color, thickness, cv2.LINE_AA)
cv2.putText(res, 'Stage 4: Frame 27', (org[0]+3*256,org[1]), font,  
            fontScale, color, thickness, cv2.LINE_AA)

cv2.imwrite("/home/drive/000000/outs/60.png", res)

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()	