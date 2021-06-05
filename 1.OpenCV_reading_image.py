import numpy as np
import matplotlib.pyplot as plt
import cv2
print("Imports are Done!")

# Reading an image in a gray scale
img = cv2.imread("my_1st_image.jpeg", cv2.IMREAD_GRAYSCALE)
# Other scales:
#IMREAD_COLOR = +1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

# Showing this image (called img) using an OpenCV build-in method (cv2.imshow), BGR colours
cv2.imshow('image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Alternatively, showing this image using a matplotlib method (plt.imshow), RGB colours
#plt.imshow(img, cmap='gray', interpolation='bicubic') # RGB
#plt.plot([50, 100], [80, 100], 'c', linewidth=5)
#plt.show()

# Optionally, write an image in the file (method cv2.imwrite)
cv2.imwrite('my_1st_im_gray.png', img)
