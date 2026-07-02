# What happens when we change pixel values?
fig, axes = plt.subplots(1, 3, figsize=(10, 3))

# Original
random_img = np.random.randint(0, 256, size=(8, 8))

axes[0].imshow(random_img, cmap='gray', vmin=0, vmax=255)
axes[0].set_title("Original")
axes[0].axis('off')

# Inverted (255 - each pixel = dark becomes light)
axes[1].imshow(255 - random_img, cmap='gray', vmin=0, vmax=255)
axes[1].set_title("Inverted (255 - pixels)")
axes[1].axis('off')

# Halved brightness
axes[2].imshow(random_img // 2, cmap='gray', vmin=0, vmax=255)
axes[2].set_title("Half brightness (÷ 2)")
axes[2].axis('off')

plt.suptitle("Images are just maths on arrays!", fontsize=13)
plt.tight_layout()
plt.show()