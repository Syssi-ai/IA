from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

print("Libraries loaded! ")

# Open the image
img = Image.open("Chaton.jpg")

# Basic info
print("Size (width x height):", img.size)
print("Mode:", img.mode)    # RGB means colour, L means grayscale
print("Format:", img.format)

# Convert image → NumPy array
img_array = np.array(img)

print("Array shape:", img_array.shape)
# Shape is (height, width, channels)
# channels = 3 for RGB (Red, Green, Blue)

print("Data type:", img_array.dtype)    # uint8 = integers from 0 to 255
print("Min pixel value:", img_array.min())
print("Max pixel value:", img_array.max())
