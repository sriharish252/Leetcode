from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])
    for i in range(len(row)):
        for j in range(len(col)):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(len(row)):
        for j in range(len(col)):
            if row[i] or col[j]:
                matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)

# Time Complexity - O(m*n) => m:rows, n:columns
# Space Complexity - O(m+n)


# Alternative O(1) Space solution:
def setZeroes_ConstantSpaceSolution(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # Idea: Use the first row and column of matrix to indicate if those rows and columns must be 0

    # Variable to store if first row of the matrix must be 0
    #   To avoid confusion if the 1st element is for row or column
    firstRow = 1

    ROWS, COLS = len(matrix), len(matrix[0])

    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == 0:
                # If checking the first row, update the firstRow variable to indicate that row is 0, 
                #   else update the 1st column in matrix
                if i == 0:
                    firstRow = 0
                else:
                    matrix[i][0] = 0
                
                # Set the column to 0
                matrix[0][j] = 0

    # Update every value except the 1st row and 1st column
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j] = 0

    if matrix[0][0]==0:
        for i in range(ROWS):
            matrix[i][0] = 0
    if firstRow==0:
        for j in range(COLS):
            matrix[0][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes_ConstantSpaceSolution(matrix)
print(matrix)

# Time Complexity - O(m*n) => m:rows, n:columns
# Space Complexity - O(1)