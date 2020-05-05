import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import Image, PIL

cap = cv2.VideoCapture('/home/drive/Downloads/golfswing2.mp4')

backSub = cv2.createBackgroundSubtractorMOG2()


while cap.isOpened():

	ret, frame = cap.read()

	if not ret:
		print("End of frames...")
		break


	#im = Image.open('image.jpg')
	#img = PIL.Image.fromarray(frame)
	# using Image.ADAPTIVE to avoid dithering
	#out = img.convert('P', palette=Image.ADAPTIVE, colors=256)

	#(h, w) = frame.shape[:2]

	#arr = np.array(img)

	b, g, r = cv2.split(frame)


	## Convert the image to L*a*b color scheme(one that is based on Euclidean distance)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	## Reshape the image into feature vector so that k-means can be applied
	#img = img.reshape((img.shape[0] * img.shape[1], 1))

	## Apply K-Means using the specified cluster size and create quantized image based on predictions
	#clt = MiniBatchKMeans(n_clusters = 8)
	#labels = clt.fit_predict(img)
	#quant = clt.cluster_centers_.astype("uint8")[labels]

	## Reshape the feature vectors into images
	#quant = quant.reshape((h, w, 1))
	#img = img.reshape((h, w, 1))

	## Convert back from L*a*b to BGR
	#quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
	#img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

	# b, g, r = cv2.split(frame)

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	cl1 = clahe.apply(g)

	fgMask = backSub.apply(cl1)

	ret3,th3 = cv2.threshold(fgMask,150,255,cv2.THRESH_BINARY)

	opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
	#displayImgs(morph2, opening, 'Opening')


	#ret3,th3 = cv2.threshold(cl1,200,255,cv2.THRESH_BINARY)


	# #gt = cv2.merge((gt,gt,gt))

	cv2.imshow("green", opening)

	k = cv2.waitKey(20)

	if k & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()