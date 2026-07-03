import matplotlib.pyplot as plt
from PIL import Image

# Your turn!
# Display the blue channel as grayscale

image = Image.open("Chaton.jpg")    
blue = image.split()[2]  # Get the blue channel

plt.imshow(blue, cmap='gray')
plt.title("Blue channel (grayscale)")
plt.axis('off')
plt.show()