import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2 as cv
import imutils

fig = plt.figure()
fig_two = plt.axes()
plt.axis('off')
img = cv.imread('tonto.png')

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

ims = []
COUNTER=0

while COUNTER<700:
    shifted = imutils.translate(img, 0, COUNTER*2.5)
    im = plt.imshow(shifted, animated=True)
    ims.append([im])
    COUNTER+=1
    # print("COUNTER ",imt)
    if COUNTER == 1000:
        break

fig_two.set_xlim(0, 400)
fig_two.set_ylim(600,20)

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)

# plt.show()
ani.save('fly_over_tonto.mp4',fps=10)
