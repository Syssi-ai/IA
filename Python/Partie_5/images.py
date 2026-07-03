import numpy as np
import matplotlib.pyplot as plt

# A hand-crafted 8x8 "image" — try to guess what it looks like!
smiley = np.array([
    [255, 255,   0,   0,   0,   0, 255, 255],
    [255,   0, 255, 255, 255, 255,   0, 255],
    [  0, 255, 0, 255, 255,   0, 255,   0],
    [  0, 255, 255, 255, 255, 255, 255,   0],
    [  0, 255,   0, 255, 255,   0, 255,   0],
    [  0, 255, 255,   0,   0, 255, 255,   0],
    [255,   0, 255, 255, 255, 255,   0, 255],
    [255, 255,   0,   0,   0,   0, 255, 255],
])

print("Array shape:", smiley.shape)
print("\nRaw numbers:")
print(smiley)

print("\nAs an image:")
plt.imshow(smiley, cmap='gray', vmin=0, vmax=255)
plt.title("A tiny 8x8 image")
plt.axis('off')
plt.show()

