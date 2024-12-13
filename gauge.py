# import matplotlib.pyplot as plt

# # Create figure and axes
# fig, ax = plt.subplots(figsize=(4, 4))

# # Define gauge parameters
# theta = np.linspace(0, 2 * np.pi, 100)
# r = 1
# x = r * np.cos(theta)
# y = r * np.sin(theta)

# # Plot the gauge outline
# ax.plot(x, y, 'k')

# # Plot the needle
# needle_angle = np.pi / 4  # Example angle
# ax.plot([0, r * np.cos(needle_angle)], [0, r * np.sin(needle_angle)], 'r', linewidth=2)

# # Set aspect ratio and remove axes
# ax.set_aspect('equal')
# ax.axis('off')

# plt.show()
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
# Load the image
# Open the image
img = Image.open("hi2.png")

# Rotate the image by 45 degrees
rotated_img = img.rotate(30)
theta = np.linspace(0, 2 * np.pi, 100)
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)

needle_angle = 90  # Example angle
# Sample data
x = [171,171]
y = [0,50]

# Create the plot
plt.plot(x, y,'r', linewidth=2)

# Display the rotated image using Matplotlib
plt.imshow(rotated_img)
plt.axis('off')  # Hide the axes
plt.show()