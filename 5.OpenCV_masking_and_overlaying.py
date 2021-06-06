import numpy as np
import cv2
print("Imports are Done!")

# Reading a base image and an OpenCV logo
img_base = cv2.imread('my_1st_im_gray.png')
img_logo = cv2.imread('opencv_logo_icon.png')
# resizing logo image to reduce its dimensions:
img_logo = cv2.resize(img_logo, (int(img_logo.shape[1] * 0.25), int(img_logo.shape[0] * 0.25)))

# Superimposing the logo with empty background
rows, cols, channels = img_logo.shape
roi = img_base[0:rows, 0:cols]

# Creating a mask of the logo
img2gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)
# add threshold
ret, mask = cv2.threshold(img2gray, 20, 255, cv2.THRESH_BINARY_INV)
# then its inverse mask
mask_inv = cv2.bitwise_not(mask) # black areas of the mask

# Black-out the area of logo in ROI (of the base image)
img_base_bg = cv2.bitwise_and(roi, roi, mask = mask)
# Take the logo region containing the logo alone
img_logo_fg = cv2.bitwise_and(img_logo, img_logo, mask = mask_inv)

# Add up background and foreground and update our base image
dst = cv2.add(img_base_bg, img_logo_fg)
img_base[0:rows, 0:cols] = dst

# Showing all the images
cv2.imshow('res', img_base)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img_base_bg', img_base_bg)
cv2.imshow('img_logo_fg', img_logo_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally, let us save the result
cv2.imwrite('resized_logo.png', img_logo)
cv2.imwrite('flowers+logo.png', img_base)
