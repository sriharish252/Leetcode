from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # k: starting index of row, l: starting index of column
    k, l = 0, 0
    # m: last index of row, n: last index of column
    m, n = (len(matrix) -1), (len(matrix[0]) -1)
    result = []

    while k<=m and l<=n:
        # Traverse top row
        for j in range(l, n+1):
            result.append(matrix[k][j])
        k+=1    # Increment starting index of row, as 1st row is traversed
        
        # Traverse right column
        for i in range(k, m+1):
            result.append(matrix[i][n])
        n-=1    # Decrement last index of column, as last column is traversed

        if not (k<=m and l<=n):
            break

        # Traverse bottom row
        for j in range(n, l-1, -1):
            result.append(matrix[m][j])
        m-=1    # Decrement last index of row, as last row is traversed

        # Traverse left column
        for i in range(m, k-1, -1):
            result.append(matrix[i][l])
        l+=1    # Increment starting column, as 1st column is traversed
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

# Time Complexity - O(m*n) => m:number of rows, n:number of columns
# Space Complexity - O(1)