
def uniquePaths(m: int, n: int) -> int:
    # 2D array to store number of unique paths at each index
    #   There's only 1 possible way at the Last row and Last column
    #   So we initialize the matrix with 1
    dp = [[1 for j in range(n)] for i in range(m)]  # n is columns, m is rows
    
    # Traversing from the bottom-right-most index to the top-left-most
    for i in range (m-2, -1, -1):
        for j in range(n-2, -1, -1):
            # Each index's possibilities is the sum of the index below and the index to the right
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp[0][0]

print(uniquePaths(3,4))

# Time Complexity - O(m*n)  => m:number of rows, m:number of columns
# Space Complexity - O(m*n)