import numpy as np

# Array of all zeros (shape: 3 rows, 4 columns)
zeros = np.zeros((3, 4))
print("Zeros:")
print(zeros)

# Array of all ones
ones = np.ones((2, 5))
print("\nOnes:")
print(ones)

# Array of random numbers between 0 and 1
random = np.random.rand(3, 3)
print("\nRandom:")
print(random)

# Random integers (e.g. pixel values 0–255)
pixels = np.random.randint(0, 124, size=(4, 4))
print("\nRandom pixel values:")
print(pixels)