'''
This is a program desgined to do resection on a raster map given its coords. N,S,E,W in lat long.
to find position

In psuedo code this is the design of the system.

input the lat long of the entire extent 

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2 as cv
import imutils

x = [1500,3025,1500,0]
y = [0,1137.5,2275,1137.5]
n = ["N","E","S","W"]

fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y[i]))

# plt.axis('off')
img = cv.imread('mapimage.jpeg')

plt.imshow(img)
plt.savefig("fig")
# plt.show()

