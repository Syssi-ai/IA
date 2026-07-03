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

# Look at a tiny patch of pixel values (top-left 5x5 corner)
print("Top-left 5x5 pixels (R values only):")
print(img_array[:5, :5, 0])    # row 0-4, col 0-4, Red channel

print("\nOne specific pixel at row 100, col 100:")
print("[R, G, B] =", img_array[100, 100])    # [R, G, B] values