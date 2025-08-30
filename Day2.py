# Transpose of a Matrix

# Write a Python function that computes the transpose of a given matrix.

# Example:
# Input:
# a = [[1,2,3],[4,5,6]]
# Output:
# [[1,4],[2,5],[3,6]]
# Reasoning:
# The transpose of a matrix is obtained by flipping rows and columns.

from typing import List, Union
def transpose_matrix(a: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    return [list(row) for row in zip(*a)]

# Example usage
if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print("Original matrix:", a)
    print("Transposed matrix:", transpose_matrix(a))