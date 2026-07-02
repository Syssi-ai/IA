import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

syssi = np.random.randint(0, 255, size=(10,10))
axes[0].imshow(syssi, cmap='gray')
axes[0].set_title("Syssi's tableau")
axes[0].axis('off')

axes[1].imshow(255 - syssi, cmap='gray')
axes[1].set_title("Inverted (255 - pixels)")
axes[1].axis('off')
plt.show()

