import numpy as np
import cv2
print("Imports are Done!")

frame = cv2.imread("my_2nd_image.png", cv2.IMREAD_GRAYSCALE)
	
# edge detectors (there are many)
edges = cv2.Canny(frame, 100, 200)

# Optional - resizing an image by preserving its aspect ratio
# percentage by which we resize our image (based on the hight)
final_height = 512 # pixels
height_ratio = final_height / edges.shape[0]
#calculate the ratio of original dimensions
height = int(edges.shape[0] * height_ratio)
width = int(edges.shape[1] * height_ratio)
# desired size
dsize = (width, height)
# resizing our image
im_res = cv2.resize(edges, dsize)
	
#cv2.imshow("original", frame)
cv2.imshow("Canny Edges", im_res)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Canny_edges_Leiden.png', im_res)