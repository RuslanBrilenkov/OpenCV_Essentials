import numpy as np
import cv2
print("Imports are Done!")

# capturing video from the 1st webcam on your computer, index=0
capt = cv2.VideoCapture(0)

# return and frame
# All the analysis of the video will be happening inside this loop
while True:
	ret, frame = capt.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# HSV = Hue, Saturation, Value
	lower_lim = np.array([5, 160, 0])
	upper_lim = np.array([10, 255, 255])
	
	# creating a mask
	mask = cv2.inRange(hsv, lower_lim, upper_lim)
	# passing the filtered color only
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	# Gaussian blur
	blur = cv2.GaussianBlur(res, (5,5), 0)
	
	# showing original, mask and filtered images
	#cv2.imshow('frame', frame)
	#cv2.imshow('mask', mask)
	#cv2.imshow('result', blur)
	
	# Show frame and filter side by side
	horiz_conc = np.concatenate((frame, blur), axis=1)
	cv2.imshow('frame & filter', horiz_conc)
	
	# press 'q' to quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cv2.destroyAllWindows()
capt.release()
