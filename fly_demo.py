import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2 as cv
import imutils

fig = plt.figure()
plt.axis('off')
img = cv.imread('mapimage.jpeg')

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

ims = []
for i in range(200):
    M = np.float32([[1, i, 25], [0, 1, 500]])
    shifted = imutils.translate(img, 0, i)
    im = plt.imshow(shifted, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=90, blit=True,
                                repeat_delay=1000)

# ani.save('fly_over.mp4')

plt.show()