import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2 as cv
import imutils
# from scipy import ndimage
from PIL import Image
import numpy as np

fig = plt.figure()
fig_two = plt.axes()
plt.axis('off')
img = Image.open('example.png')

img_array = np.array(img)
height, width = img_array.shape[:2]
print(f"Image dimensions: {width}x{height} pixels")

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

# Add angle management class
class HeadingAngle:
    def __init__(self, initial_angle=0):
        self._angle = initial_angle
    
    def get_angle(self):
        return self._angle
    
    def set_angle(self, new_angle):
        self._angle = new_angle % 360  # Keep angle within 0-360 range
        heading_indi(self._angle)  # Update heading indicator

# Replace global angle with HeadingAngle instance
heading = HeadingAngle()

rotation_speed = 1.5  # Degrees to rotate per key press

# Create a separate figure and axes for the heading indicator
heading_fig = plt.figure()
heading_ax = heading_fig.add_subplot(111)
heading_ax.axis('off')

def heading_indi(deg):
    heading_ax.clear()  # Clear previous content
    img = Image.open("hi2.png")
    rotated_img = img.rotate(deg)
    
    # Sample data for line
    x = [171, 171]
    y = [0, 50]
    
    # Update the plot
    heading_ax.plot(x, y, 'r', linewidth=2)
    heading_ax.imshow(rotated_img)
    heading_ax.axis('off')
    plt.draw()  # Update the figure

# Add keyboard event handler
def on_key(event):
    if event.key == 'left':
        heading.set_angle(heading.get_angle() - rotation_speed)
        plt.figure(heading_fig.number)  # Switch to heading figure
        heading_indi(heading.get_angle())  # Force update
        plt.figure(fig.number)  # Switch back to main figure
    elif event.key == 'right':
        heading.set_angle(heading.get_angle() + rotation_speed)
        plt.figure(heading_fig.number)  # Switch to heading figure
        heading_indi(heading.get_angle())  # Force update
        plt.figure(fig.number)  # Switch back to main figure

# Connect key event handler to both figures
fig.canvas.mpl_connect('key_press_event', on_key)
heading_fig.canvas.mpl_connect('key_press_event', on_key)

# Make sure both figures are visible
plt.figure(fig.number)  # Switch back to main figure
im = plt.imshow(img)

def translate_image(image, x_shift, y_shift):
    """Translates the image by the specified amount in x and y directions."""
    img_array = np.array(image)
    M = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    shifted = cv.warpAffine(img_array, M, (width, height))
    return shifted

def update(frame):
    shifted = translate_image(img, 0, -frame)
    shifted_pil = Image.fromarray(shifted)
    rotated = shifted_pil.rotate(heading.get_angle())
    rotated_array = np.array(rotated)
    
    im.set_array(rotated_array)
    return [im]

heading_indi(heading.get_angle())
# Add key binding before animation creation
fig.canvas.mpl_connect('key_press_event', on_key)
ani = animation.FuncAnimation(fig, update, frames=range(0, height, 5),
                            interval=50, blit=False)

fig_two.set_xlim(10, width/2)
fig_two.set_ylim(0,height/3)

plt.show()
# ani.save('fly_over_tonto.mp4',fps=10)
