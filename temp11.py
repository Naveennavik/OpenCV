import cv2
import numpy as np

cap1 = cv2.VideoCapture('/home/drive/Downloads/zav2/openpose/output/cricket_sample_outputs/cricket_sample.mp4')

cap2 = cv2.VideoCapture('/home/drive/Downloads/CRICKET_60fps.mp4')

cap3 = cv2.VideoCapture('/home/drive/Downloads/cricket_sample_2d_21.mp4')

cap4 = cv2.VideoCapture('/home/drive/Downloads/cricket_1.mp4')


cond = cap1.isOpened() and cap2.isOpened()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('/home/drive/Downloads/cricket_combined_3.mp4',fourcc, 60, (1920, 1080))

font = cv2.FONT_HERSHEY_COMPLEX 
org = (1700, 78)
fontScale = 0.8
color = (255,255,255)
#color = (0,145,245)
thickness = 2

count = 0
#print(cond)

def resizeImg():
	add1 = cv2.imread("/home/drive/Downloads/stage_ids/orgvd_.jpg")
	add2 = cv2.imread("/home/drive/Downloads/stage_ids/3dorg_.jpg")

	nh = 50
	nw = 200

	#add1 = cv2.resize(add1, (nw, nh))
	#add2 = cv2.resize(add2, (nw, nh))

	return add1, add2

while cond:

	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()
	ret3, frame3 = cap3.read()
	ret4, frame4 = cap4.read()
	
	res = np.zeros((1080,1920,3),np.uint8)
	
	ret = ret1 and ret2 and ret3 and ret4

	if not ret:
		print("End of frames...")
		break

	'''
	frame1 = cv2.putText(frame1, 'Original', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

	frame2 = cv2.putText(frame2, '2d Joints', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    

	frame3 = cv2.putText(frame3, '3D Reconstruction', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    

    
	concat_h1 = np.hstack((frame1[104:744,:], frame2[104:744,:]))
	concat_h2 = np.hstack((frame3[104:744,:], frame4[104:744,:]))

	concat = np.vstack((concat_h1, concat_h2))

	concat = cv2.line(concat, (480,0), (480,640*2), (255,255,255), 1)
	concat = cv2.line(concat, (0,640), (480*2,640), (255,255,255), 1)

	concat = cv2.line(concat, (480*2,0), (480*2,640*2), (255,255,255), 2) 
	concat = cv2.line(concat, (0,640*2), (480*2,640*2), (255,255,255), 2)

	concat = cv2.rectangle(concat, (0,0), (480*2,640*2), (255,255,255), 1)

	'''

	concat = np.hstack((frame1, frame2, frame3, frame4))
	#concat = cv2.rectangle(concat, (0,0), (1920,1080), (125,125,125), 2)
	res[116:116+848,:] = concat

	#print(concat.shape)

	#text = "Frame: " + str(count)

	#concat = cv2.putText(concat, text, org, font,  
                   		#fontScale, color, thickness, cv2.LINE_AA)

		
	count += 1
	out.write(res)
	cv2.imshow("Concat", res)

	
	k = cv2.waitKey(20)

	if k & 0xFF == 27:
		break

	

#out.release()

cap1.release()
cap2.release()
cap3.release()
cap4.release()

cv2.destroyAllWindows()

