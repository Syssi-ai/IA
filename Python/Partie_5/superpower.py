import numpy as np

scores = np.array([88, 72, 95, 60, 83])

# Do maths on the whole array at once — no loop needed!
print("Original:", scores)
#print("+ 5 bonus points:", scores + 5)
scores = scores + 5
print("Original:", scores)
print("Doubled:", scores * 2)
print("As percentage of 100:", scores / 100)

# Statistics
print("\nMin:", scores.min())
print("Max:", scores.max())
print("Mean:", scores.mean())
print("Sum:", scores.sum())