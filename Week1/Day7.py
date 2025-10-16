import numpy as np

# --- Task 1: Create a 3x3 matrix using np.arange() ---
matrix = np.arange(9).reshape(3, 3)
print("Matrix:\n", matrix)

# Print shape, size, and dimensions
print("Shape of matrix:", matrix.shape)
print("Size of matrix:", matrix.size)
print("Number of dimensions:", matrix.ndim)


# --- Task 2: Generate 100 random numbers and find mean & std deviation ---
random_numbers = np.random.normal(loc=0, scale=1, size=100)

print("\nRandom numbers:\n", random_numbers)
print("Mean:", np.mean(random_numbers))
print("Standard Deviation:", np.std(random_numbers))
