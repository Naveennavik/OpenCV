'''
Merge Videos

'''

import cv2
import numpy as np

cap1 = cv2.VideoCapture('/home/drive/Downloads/zav2/openpose/sample_ip/56.mp4')
#cap2 = cv2.VideoCapture('/home/drive/Downloads/zav2/openpose/21_final_op/fully_perfect/60.mp4')
cap3 = cv2.VideoCapture('/home/drive/000000/inputs/56_vibe_result_mesh.mp4')
#cap4 = cv2.VideoCapture('/home/drive/Downloads/anim_output.mp4')
frame4 = cv2.imread("/home/drive/000000/outs/60.png")
#print(f4.shape)

cond = cap1.isOpened() and cap3.isOpened()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('/home/drive/Downloads/sample_ip/out250.mp4',fourcc, 16, (1280, 720*3))
out = cv2.VideoWriter('/home/drive/Downloads/sample_ip/test56z.mp4',fourcc, 25, (1280, 720*2))

font = cv2.FONT_HERSHEY_DUPLEX 
org = (1020, 150)
fontScale = 1
#color = (255,255,255)
color = (0,145,245)
thickness = 2

count = 0
#print(cond)

def resizeImg():
	add1 = cv2.imread("/home/drive/Downloads/stage_ids/Original_Video.jpg")
	#/home/drive/Downloads/stage_ids/Original_Video.jpg
	add2 = cv2.imread("/home/drive/Downloads/stage_ids/Body_Pose.jpg")
	add3 = cv2.imread("/home/drive/Downloads/stage_ids/3D_Object.jpg")
	add4 = cv2.imread("/home/drive/Downloads/stage_ids/Key_Stages.jpg")

	'''
	nh = 50
	nw = 250

	add1 = cv2.resize(add1, (nw, nh))
	add2 = cv2.resize(add2, (nw, nh))
	add3 = cv2.resize(add3, (nw, nh))
	add4 = cv2.resize(add4, (nw, nh))
	'''

	return add1, add2, add3, add4

while cond:

	ret1, frame1 = cap1.read()
	#ret2, frame2 = cap2.read()
	ret3, frame3 = cap3.read()
	#ret4, frame4 = cap3.read()

	frame1 = np.zeros((frame3.shape),np.uint8)
	#ret = ret1 and ret2 and ret3
	ret = ret1 and ret3

	if not ret:
		print("End of frames...")
		break

	#wid3 = 642
	#hei3 = 800
	#new_dim = (wid3, hei3)

	#Resize the image:
	#frame3 = cv2.resize(frame3, new_dim)

	
	#frame4 = np.zeros((720, 1280, 3), np.uint8)

	'''
	frame1 = cv2.putText(frame1, 'Original', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

	frame2 = cv2.putText(frame2, '2d Joints', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    

	frame3 = cv2.putText(frame3, '3D Reconstruction', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    '''
    
	add1, add2, add3, add4 = resizeImg()

	
	frame1[50:100, 50:300] = add1
	#frame2[50:100, 50:300] = add2
	frame3[50:100, 50:300] = add3
	#frame4[50:100, 50:300] = add4
	

	#concat1 = np.vstack((frame1, frame2))
	#concat2 = np.vstack((frame3, frame4))

	#concat = np.hstack((concat1, concat2))

	concat = np.vstack((frame1, frame3))

	text = "Frame: " + str(count)

	#concat = cv2.putText(concat, text, org, font,  
                   		#fontScale, color, thickness, cv2.LINE_AA)
	
	cv2.line(concat, (0,720), (2560,720), (255, 255, 255), 4)
	#cv2.line(concat, (1280,0), (1280,1440), (255, 255, 255), 4)
	#cv2.line(concat, (1600,0), (1600,800), (255, 255, 255), 1)

	count += 1
	out.write(concat)
	cv2.imshow("Concat", concat)

	
	k = cv2.waitKey(20)

	if k & 0xFF == 27:
		break

	

out.release()

cap1.release()
#cap2.release()
cap3.release()

cv2.destroyAllWindows()

