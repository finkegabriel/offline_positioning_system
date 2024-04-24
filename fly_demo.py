import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2 as cv
import imutils


fig = plt.figure()
fig_two = plt.axes()
plt.axis('off')
img = cv.imread('mapimage.jpeg')

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

ims = []
for i in range(100):
    shifted = imutils.translate(img, 0, i*2.5)
    im = plt.imshow(shifted, animated=True)
    ims.append([im])

fig_two.set_xlim(1000, 500)
fig_two.set_ylim(2000,500)
ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True)

ani.save('fly_over.mp4',fps=10)

plt.show()