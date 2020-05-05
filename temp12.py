import cv2
import numpy as np
import glob

#cap1 = cv2.VideoCapture("/home/drive/Downloads/zav2/openpose/output/cricket_sample_outputs/cricket_sample_25pts.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/drive/Downloads/zav2/VIBE/process_imgs/naveen_staf_2_mp4_output/out.mp4',fourcc, 30, (1080,1920))

count = 0

#cap2 = cv2.VideoCapture("/home/drive/Downloads/cricket_sample_vibe.mp4")

#fnames = glob.glob("/home/drive/Downloads/zav2/VIBE/process_imgs/cricket_sample_mp4_output/masks/*.png")
fnames = glob.glob("/home/drive/Downloads/zav2/VIBE/process_imgs/naveen_staf_2_mp4_output/masks/*.png")
#print(fnames[0][:-13])
#print(fnames[0].split('/')[-1].split('_')[0][-3:])
#/home/drive/Downloads/zav2/VIBE/process_imgs/cricket_sample_mp4_output/masks/000000_mask.png
def reorder(fnames):

	nums = []
	for fname in fna mes:
		nums.append(int(fname.split('/')[-1].split('_')[0][-3:]))

	nums.sort()
	#print(nums)
	filnames = []
	for i, num in enumerate(nums):
		if len(str(num)) == 1:
			filnames.append(fnames[0][:-13] + '00' + str(num) + '_imask.png')
		elif len(str(num)) == 2:
			filnames.append(fnames[0][:-13] + '0' + str(num) + '_imask.png')
		else:
			filnames.append(fnames[0][:-13] + str(num) + '_imask.png')

	return filnames

filnames = reorder(fnames)
print(filnames[0])
print(len(filnames))


for i in range(1,len(filnames)+1):
	
	img = cv2.imread(filnames[count])
	#print(frame2.shape)

	#img = cv2.addWeighted(frame1, 1.0, frame2, 1.0, 0)
	#img = frame2
	cv2.imshow('image', img)
	count += 1

	out.write(img)
	print(count)
	k = cv2.waitKey(20)

	if k & 0xFF == 27:
		break


out.release()
cv2.destroyAllWindows()

print("1: ", count)