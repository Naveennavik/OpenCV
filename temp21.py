'''
Generate grid texture

'''

import cv2
import numpy as np
import glob

#input_folder = '/home/drive/Downloads/Myntra3/'
input_folder = 'C:/Users/NAVIK/Desktop/empty/'
files = glob.glob(input_folder + "[S][t][d][_]*[ye].*")

#print(len(files))

img_dict = {}

img_2048 = ['Std_Skin_Arm_diffuse', 'Std_Skin_Body_diffuse', 'Std_Skin_Head_diffuse', 'Std_Skin_Leg_diffuse']
img_1024 = ['Std_Eyelash_opacity','Std_Cornea_L_diffuse','Std_Eye_L_diffuse','Std_Upper_Teeth_diffuse',
'Std_Lower_Teeth_diffuse','Std_Cornea_R_diffuse','Std_Eye_R_diffuse','Std_Tongue_diffuse','Std_Nails_diffuse']

out_file1 = input_folder + 'grids1.jpg'
out_file2 = input_folder + 'grids1.png'


for file in files:
	print(file)

	k = file.split('\\')[-1].split('.')[0]
	#k = file.split('.')[1]
	print(k)

	if k not in img_1024 and k not in img_2048:
		continue
	img_dict[k] = cv2.imread(file)

	if k in img_1024 and img_dict[k].shape != (1024,1024,3):
		img_dict[k] = cv2.resize(img_dict[k], dsize=(1024,1024))

	if k in img_2048 and img_dict[k].shape != (2048,2048,3):
		img_dict[k] = cv2.resize(img_dict[k], dsize=(2048,2048))

print("Total imgs: ", len(img_dict.keys()))

#final_img = np.zeros((1024*6,1024*5,3), np.uint8)
black_1 = np.zeros((1024,1024,3),np.uint8)
black_2 = np.vstack((black_1,black_1))

hs_1 = np.hstack((img_dict['Std_Eyelash_opacity'], img_dict['Std_Cornea_L_diffuse'], img_dict['Std_Eye_L_diffuse'], 
	img_dict['Std_Upper_Teeth_diffuse'], img_dict['Std_Lower_Teeth_diffuse'],black_1))
hs_2 = np.hstack((black_1, img_dict['Std_Cornea_R_diffuse'], img_dict['Std_Eye_R_diffuse'], 
	img_dict['Std_Tongue_diffuse'], img_dict['Std_Nails_diffuse'], black_1))

hs_3 = np.hstack((black_2, img_dict['Std_Skin_Arm_diffuse'], img_dict['Std_Skin_Body_diffuse'], black_2))
hs_4 = np.hstack((black_2, img_dict['Std_Skin_Head_diffuse'], img_dict['Std_Skin_Leg_diffuse'], black_2))

final_img = np.vstack((hs_1,hs_2,hs_3,hs_4))

cv2.imwrite(out_file1, final_img)
cv2.imwrite(out_file2, final_img)







	