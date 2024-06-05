from typing import List

def numIslands(self, grid: List[List[str]]) -> int:
    # IDEA: Iterate through all cells in the grid,
    #       Perform DFS from every node with 1, where 
    #           every neighboring 1s are changed to 0
    #       If a new 1 is found after the initial DFS,
    #           increase the island count and 
    #           repeat till you reach the last cell in the grid
    
    ROWS, COLS = len(grid), len(grid[0])
    islandCount = 0

    def assignSameIslandToZero(i: int, j:int):
        if i<0 or i>=ROWS or j<0 or j>=COLS or grid[i][j]=="0":
            return
        grid[i][j] = "0"
        assignSameIslandToZero(i+1, j)
        assignSameIslandToZero(i-1, j)
        assignSameIslandToZero(i, j+1)
        assignSameIslandToZero(i, j-1)
        return
    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]=="1":
                islandCount += 1
                assignSameIslandToZero(i, j)
    return islandCount


# Time Complexity - O(m*n) => m: number of rows, n:number of columns
# Space Complexity - O(1)