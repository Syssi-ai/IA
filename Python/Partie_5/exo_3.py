import numpy as np
import matplotlib.pyplot as plt

# Your turn! Change the numbers to draw something.
# 0 = black, 255 = white, 128 = grey

my_art = np.array([
    [  0,   0,   0,   0,   0,   0],
    [  0, 128, 128, 128, 128,   0],
    [  0, 128,   0,   0, 128,   0],
    [  0, 128,   0,   0, 128,   0],
    [  0, 128, 128, 128, 128,   0],
    [  0,   0,   0,   0,   0,   0],
])

plt.imshow(my_art, cmap='gray', vmin=0, vmax=255)
plt.title("My pixel art")
plt.axis('off')
plt.show()

print("Min brightness:", my_art.min())
print("Max brightness:", my_art.max())
print("Average brightness:", my_art.mean())