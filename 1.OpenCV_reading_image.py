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

# Optional - resizing an image by preserving its aspect ratio
# percentage by which we resize our image (based on the hight)
final_height = 512 # pixels
height_ratio = final_height / img.shape[0]
#calculate the ratio of original dimensions
height = int(img.shape[0] * height_ratio)
width = int(img.shape[1] * height_ratio)
# desired size
dsize = (width, height)
# resizing our image
im_res = cv2.resize(img, dsize)

# printing out the resized image dimensions for confirmation
print("Resized image has hight = {}, width = {}".format(im_res.shape[0], im_res.shape[1]))

# Showing this image using an OpenCV build-in method (cv2.imshow), BGR colours
cv2.imshow('image', im_res) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Alternatively, showing this image using a matplotlib method (plt.imshow), RGB colours
#plt.imshow(im_res, cmap='gray', interpolation='bicubic') # RGB
#plt.plot([50, 100], [80, 100], 'c', linewidth=5)
#plt.show()

# Optionally, write an image in the file (method cv2.imwrite)
cv2.imwrite('my_1st_im_gray.png', im_res)
