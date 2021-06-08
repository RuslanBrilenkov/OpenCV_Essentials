import numpy as np
import cv2
print("Imports are Done!")

image = cv2.imread("my_2nd_image.png", cv2.IMREAD_GRAYSCALE)

# average the pixels
kernel = np.ones((5, 5), np.float32)/(5**2)
smoothed = cv2.filter2D(image, -1, kernel)

# Gaussian blur
blur = cv2.GaussianBlur(image, (5,5), 0)

# Median Blur
median = cv2.medianBlur(image, 5)

# bilateral filter
bilateral = cv2.bilateralFilter(image, 5, 75, 75)

font = cv2.FONT_HERSHEY_SIMPLEX

#cv2.putText(image, 'image', (20,50), font, 2, (0, 245, 256), 2, cv2.LINE_AA)
#cv2.imshow('image', image)
cv2.putText(smoothed, 'smoothed', (20,50), font, 2, (0, 245, 256), 2, cv2.LINE_AA)
cv2.imshow('smoothed', smoothed)
cv2.putText(blur, 'blur', (20,50), font, 2, (0, 245, 256), 2, cv2.LINE_AA)
cv2.imshow('blur', blur)
cv2.putText(median, 'median', (20,50), font, 2, (0, 245, 256), 2, cv2.LINE_AA)
cv2.imshow('median', median)
cv2.putText(bilateral, 'bilateral', (20,50), font, 2, (0, 245, 256), 2, cv2.LINE_AA)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Combining in one collage:
horiz_conc1 = np.concatenate((smoothed, blur), axis=1)
horiz_conc2 = np.concatenate((median, bilateral), axis=1)
horiz_conc = np.concatenate((horiz_conc1, horiz_conc2), axis=0)

# Optional - resizing an image by preserving its aspect ratio
# percentage by which we resize our image (based on the hight)
final_height = 512 # pixels
height_ratio = final_height / horiz_conc.shape[0]
#calculate the ratio of original dimensions
height = int(horiz_conc.shape[0] * height_ratio)
width = int(horiz_conc.shape[1] * height_ratio)
# desired size
dsize = (width, height)
# resizing our image
im_res = cv2.resize(horiz_conc, dsize)

cv2.imwrite('Leiden_horiz_conc.png', im_res)

