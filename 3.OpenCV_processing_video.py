import numpy as np
import cv2
print("Imports are Done!")

# capturing video from the 1st webcam on your computer, index=0
capt = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.mp3',fourcc, 20.0, (640, 480))

# return and frame
# All the analysis of the video will be happening inside this loop
while True:
	ret, frame = capt.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	
	#cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


capt.release()
out.release()
cv2.destroyAllWindows()
