import numpy as np

grid = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print("Top-left corner (row 0, col 0):", grid[0, 0])    # 1
print("Middle value (row 1, col 2):", grid[1, 2])        # 7
print("Bottom-right (row 2, col 3):", grid[2, 3]) 
print("Une des valeurs:", grid[2, 1])       # 12

# Get a full row
print("\nEntire first row:", grid[0])      # [1 2 3 4]
print("Entire last row:", grid[-1])        # [9 10 11 12]

# Get a full column
print("\nEntire first column:", grid[:, 0])   # [1 5 9]
print("Dernière colonne:", grid[:, -1])
