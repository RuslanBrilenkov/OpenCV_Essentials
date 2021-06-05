import numpy as np
import cv2
print("Imports are Done!")

# Reading image:
img = cv2.imread("poor_photo_book.jpg")

# 1. Simple threshold
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# 2. The same but on grayscale image
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# 3. Gaussian adaptive threshold
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# 4. Otsu's threshold
retval3, otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Showing all of the images
cv2.imshow("original", img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("gauss", gaus)
cv2.imshow("otsu", otsu)
cv2.waitKey(0) # waiting for any key to call
cv2.destroyAllWindows()

# Saving the original and the gaussian adaptive threshold side by side:
horiz_conc = np.concatenate((grayscaled, gaus), axis=1)
cv2.imwrite('gaus_adpt_thrsh.png', horiz_conc)
