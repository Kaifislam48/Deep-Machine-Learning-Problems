# Matrix-Vector Dot Product

# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

# Example:
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]
# Reasoning:
# Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (1 * 2) + (2 * 4) = 2 + 8 = 10

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if not a or not b or len(a[0]) != len(b):
        return -1
    return [sum(x * y for x, y in zip(row, b)) for row in a]


# Example usage:
a = [[1, 2], [2, 4]]
b = [1, 2]
result = matrix_dot_vector(a, b)

print("Matrix:", a)
print("Vector:", b)
print("Dot Product Result:", result)