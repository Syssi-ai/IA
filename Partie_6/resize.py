from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Chaton.jpg")  

# Resize the image
img_small = img.resize((64, 64))
img_medium = img.resize((128, 128))

fig, axes = plt.subplots(1, 3, figsize=(9, 3))

axes[0].imshow(img)
axes[0].set_title(f"Original\n{img.size}")
axes[0].axis('off')

axes[1].imshow(img_medium)
axes[1].set_title("128 × 128")
axes[1].axis('off')

axes[2].imshow(img_small)
axes[2].set_title("64 × 64")
axes[2].axis('off')

plt.suptitle("The model always gets the same size input!", fontsize=15)
plt.tight_layout()
plt.show()