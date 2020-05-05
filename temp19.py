'''
Resize multiple images inside a folder

'''

import numpy as np
import cv2
import glob

folder = "/home/drive/8_frames/"
input_imgs = glob.glob(folder + "*.jpg")

for input_img in input_imgs:

	img = cv2.imread(input_img)
	#print("Original dimensions: ",img.shape)

	
	width = 1080
	height = 1080
	new_dim = (width, height)

	#Resize the image:
	resized = cv2.resize(img, new_dim)
	#print("New dimensions: ",resized.shape)

	out_img = folder[:-2] + '/' + input_img.split('/')[-1]

	cv2.imwrite(input_img, resized)

	#Display the image
	#cv2.imshow("Resized image", resized)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()