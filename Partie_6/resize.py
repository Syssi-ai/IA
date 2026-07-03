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

#plt.suptitle("The model always gets the same size input!", fontsize=15)
#plt.tight_layout()
#plt.show()

# Convert to grayscale
img_gray = img.convert('L')    # 'L' = luminance = grayscale

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 8))
ax1.imshow(img)
ax1.set_title(f"RGB — shape: {np.array(img).shape}")
ax1.axis('off')
ax2.imshow(img_gray, cmap='gray')
ax2.set_title(f"Grayscale — shape: {np.array(img_gray).shape}")
ax2.axis('off')
plt.tight_layout()
plt.show()


# Normalise pixel values from 0-255 to 0-1
img_array = np.array(img_small)           # shape: (64, 64, 3)
img_norm  = img_array / 255.0             # divide every pixel by 255

print("Before normalisation:")
print("  dtype:", img_array.dtype)
print("  min:", img_array.min(), " max:", img_array.max())

print("\nAfter normalisation:")
print("  dtype:", img_norm.dtype)
print("  min:", img_norm.min().round(6), " max:", img_norm.max().round(5))

print("\nShape stays the same:", img_norm.shape)