from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Chaton.jpg")  

img_array = np.array(img).astype(np.float64)    # use float so we don't overflow

# Brightness: multiply pixel values
bright = np.clip(img_array * 1.5, 0, 255).astype(np.uint8)
dark   = np.clip(img_array * 0.5, 0, 255).astype(np.uint8)

# Invert: flip all values
inverted = (255 - img_array).astype(np.uint8)

fig, axes = plt.subplots(1, 4, figsize=(14, 4))
for ax, image, title in zip(axes,
    [img_array.astype(np.uint8), bright, dark, inverted],
    ["Original", "Bright (× 1.5)", "Dark (× 0.5)", "Inverted (255 - x)"]):
    ax.imshow(image)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()