from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # left-most edge is 0 index and right-most index is the len of matrix
    left, right = 0, (len(matrix[0]) -1)
    
    while left < right:
        # Traverse through the elements in the top row except the right-most index
        #   Rotate through the corners of the square matrix in clockwise direction
        for i in range(right-left):
            top, bottom = left, right   # Since it's a square nxn matrix, bottom-most is same as right-most
            
            # Store TopLeft value in a temp variable
            tempTopLeftValue = matrix[top][left+i]
            # Move BottomLeft to TopLeft
            matrix[top][left+i] = matrix[bottom-i][left]
            # Move BottomRight to BottomLeft
            matrix[bottom-i][left] = matrix[bottom][right-i]
            # Move TopRight to BottomRight
            matrix[bottom][right-i] = matrix[top+i][right]
            # Move TopLeft (in Temp variable) to TopRight
            matrix[top+i][right] = tempTopLeftValue
        
        # Move the left, right and thereby top and bottom pointers to the next inner square
        left +=1
        right -=1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)

# Time Complexity - O(n^2) => n:number of rows or columns
# Space Complexity - O(1)