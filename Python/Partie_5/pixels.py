import numpy as np

tiny_image = np.array([
    [ 10,  50, 200, 255],
    [  0,  30, 180, 220],
    [100, 150,  80,  45],
    [255, 200, 120,  90]
])

# 1. Shape
print("Shape:", tiny_image.shape)

# 2. Pixel at row 2, col 3
print("Pixel [2,3]:", tiny_image [2,3])

# 3. Brightest pixel
print("Brightest:", tiny_image.max())

# 4. Average brightness
print("Average:", tiny_image.mean())