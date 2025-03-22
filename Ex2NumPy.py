import numpy as np

# Create two 3x3 matrices with random numbers between 1 and 10.
# Do the following:
#   - Add the two matrices.
#   - Product the two matrices.
#   - Calculate the determinant of both matrices and print the largest.
#   - Transpose both matrices.

def init_matrix():
    mat_1 = np.random.randint(1, 101, size = (3, 3))
    mat_2 = np.random.randint(1, 101, size = (3, 3))
    print("My first matrix is:\n", mat_1, "\n")
    print("My second matrix is\n", mat_2, "\n")
    return mat_1, mat_2

def sum(mat_1, mat_2): 
    return mat_1 + mat_2

def product(mat_1, mat_2):
    return mat_1 @ mat_2

def determinant(mat):
    return (int)(np.linalg.det(mat))

def transpose(mat):
    return mat.T

def printMatrix(mat_1, mat_2):
    print("The sum of mat_1 and mat_2 is:\n", sum(mat_1, mat_2))
    print("\nThe matrix product of mat_1 and mat_2 is:\n", product(mat_1, mat_2))
    print("\nThe determinant of mat_1 is:", determinant(mat_1))
    print("\nThe determinant of mat_2 is:", determinant(mat_2))
    print("\nThe transpose matrix of mat_1 is:\n", transpose(mat_1))
    print("\nThe transpose matrix of mat_2 is:\n", transpose(mat_2))


mat_1, mat_2 = init_matrix()
printMatrix(mat_1, mat_2)