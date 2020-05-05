'''
Create 2048*4,2048*4 texture grid

'''
import cv2
import numpy as np
import glob

files = glob.glob("/home/drive/Downloads/Virat_Kohli/[S][t][d][_]*[ye].*")

print(len(files))

img_dict = {}

for file in files:
	k = file.split('/')[-1].split('.')[0]
	img_dict[k] = cv2.imread(file)

	if img_dict[k].shape != (2048, 2048, 3):
		img_dict[k] = cv2.resize(img_dict[k], (2048,2048))
		print(k, img_dict[k].shape)

out_file1 = '/home/drive/Downloads/Virat_Kohli/grids.jpg'
out_file2 = '/home/drive/Downloads/Virat_Kohli/grids.png'
black = np.zeros((2048,2048,3),np.uint8)

vstack1 = np.vstack((img_dict['Std_Eyelash_opacity'],img_dict['Std_Tongue_diffuse'],
		img_dict['Std_Skin_Leg_diffuse'],img_dict['Std_Nails_diffuse']))
vstack2 = np.vstack((img_dict['Std_Cornea_L_diffuse'],img_dict['Std_Cornea_R_diffuse'],
		img_dict['Std_Skin_Arm_diffuse'],black))
vstack3 = np.vstack((img_dict['Std_Eye_L_diffuse'],img_dict['Std_Eye_R_diffuse'],
		img_dict['Std_Skin_Body_diffuse'],black))
vstack4 = np.vstack((img_dict['Std_Lower_Teeth_diffuse'],img_dict['Std_Upper_Teeth_diffuse'],
		img_dict['Std_Skin_Head_diffuse'],black))

hstack1 = np.hstack((vstack1,vstack2,vstack3,vstack4))
print(hstack1.shape)

cv2.imwrite(out_file1, hstack1)
cv2.imwrite(out_file2, hstack1)

'''
cv2.imshow('some',img_dict['Std_Eyelash_opacity'])
cv2.waitKey(0)
cv2.destroyAllWindows()
'''