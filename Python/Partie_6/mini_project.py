from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

dessin = Image.open("Veau.jpg")  #  Your turn! Try any effect you like.

def traitement_image(img):
    img = img.resize((64, 64))
    img_gray = img.convert("L")    
    np_img = np.array(img_gray) / 255.0
    return np_img

print(traitement_image(dessin))
print("MIN:", traitement_image(dessin).min())
print("MAX:", traitement_image(dessin).max())
plt.imshow(traitement_image(dessin), cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()