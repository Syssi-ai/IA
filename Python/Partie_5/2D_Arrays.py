import numpy as np

grid = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print("Grid:")
print(grid)
print("\nShape:", grid.shape)    # (3, 4) → 3 rows, 4 columns
print("Total elements:", grid.size)