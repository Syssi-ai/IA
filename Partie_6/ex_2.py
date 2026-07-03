from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Veau.jpg")  #  Your turn! Try any effect you like.


img_array = np.array(img).copy()    # .copy() so we don't change the original

# Example: swap red and blue channels
swapped = img_array.copy()
swapped[:, :, 0] = img_array[:, :, 2]    # put Blue in Red's place
swapped[:, :, 2] = img_array[:, :, 0]    # put Red in Blue's place

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(img_array)
ax1.set_title("Original")
ax1.axis('off')
ax2.imshow(swapped)
ax2.set_title("Red & Blue swapped")
ax2.axis('off')
plt.tight_layout()
plt.show()

# Now try your own effect below!
