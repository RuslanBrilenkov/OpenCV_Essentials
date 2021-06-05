import numpy as np
import cv2
print("Imports are Done!")

# Reading image:
img = cv2.imread('my_1st_im_gray.png', cv2.IMREAD_COLOR)

# BGR colors
# (255, 0, 0) is Blue
# (0, 255, 0) is Green
# (0, 0, 255) is Red
# (0, 0, 0) is Black
# (255, 255, 255) is White

# Drawing on top of our image
cv2.line(img, (100,256), (150, 300), (255, 0, 0), 5)
cv2.line(img, (150, 300), (150, 280), (255, 0, 0), 5)
cv2.line(img, (150, 300), (130, 300), (255, 0, 0), 5)

cv2.rectangle(img, (30,350), (300, 450), (0, 255, 0), 8)
cv2.circle(img, (230,100), 67, (150, 20, 200), -1)

# arbitrary shape - polygon
pts = np.array([[20,25], [52,30], [216,20], [300,500], [130,60]], np.int32)
#pts = pts.reshape((-1,1,2)) # from documentation
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# Writing on the images
# chasing font: normal size sans-serif font
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'This is flower!', (10,256), font, 1, (0, 0, 256), 4, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0) # waiting for any key to close
cv2.destroyAllWindows()

# Saving the resulting image
cv2.imwrite('my_1st_im_geometry.png', img)
