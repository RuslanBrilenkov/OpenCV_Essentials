import numpy as np
import cv2
print("Imports are Done!")

cascade_name = 'haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(cascade_name)

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	# detecting eyes
	eyes = eye_cascade.detectMultiScale(gray)
	for (ex, ey, ew, eh) in eyes:
		cv2.circle(img, ((ex+ew//2), (ey+eh//2)), 40, (255,255,0), 2)
			
	# showing a video capture
	cv2.imshow('img', img)
	
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		# a quick resizing
		dsize = (800,512)
		im_res = cv2.resize(img, dsize)
		# saving the final image from the video capture
		cv2.imwrite('Eyes_detection.png', im_res)
		break
		
		
cap.release()
cv2.destroyAllWindows()
