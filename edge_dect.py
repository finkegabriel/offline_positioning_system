import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('mapimage.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,450)

plt.imshow(edges,cmap = 'gray')


plt.axis('off')
plt.savefig("mapimage_output",transparent = True, bbox_inches = 'tight', pad_inches = 0)
plt.close()