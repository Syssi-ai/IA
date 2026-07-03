import numpy as np
import matplotlib.pyplot as plt

tableau = np.random.randint(0, 100, size=(5, 5))
plt.imshow(tableau, cmap='gray', vmin=0, vmax=100)
plt.title("Tableau 5x5 Array")
plt.axis('off')
plt.show()

print("Min value:", tableau.min())
print("Max value:", tableau.max())
print("Average value:", tableau.mean())

tableau = tableau + 10
print("\nAfter adding 10 to each element:")
plt.imshow(tableau, cmap='gray', vmin=0, vmax=100)
plt.title("Tableau after adding 10")
plt.axis('off')
plt.show() 