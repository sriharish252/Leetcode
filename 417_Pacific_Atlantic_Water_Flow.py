from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # Stores the indices of elements that can reach pacific and atlantic respectively
        pacificSet, atlanticSet = set(), set()

        # visitSet: stores the indices of elements which can be reached
        # prevHeight: stores the height of the previous node, so that 
        #               we can check if a downstream from the current node exists
        def dfs(rowIndex, colIndex, visitSet, prevHeight):
            if (
                rowIndex<0 or rowIndex>=ROWS or colIndex<0 or colIndex>=COLS or
                (rowIndex, colIndex) in visitSet or
                heights[rowIndex][colIndex] < prevHeight                
            ):
                return
            visitSet.add((rowIndex, colIndex))
            dfs(rowIndex-1, colIndex, visitSet, heights[rowIndex][colIndex])
            dfs(rowIndex+1, colIndex, visitSet, heights[rowIndex][colIndex])
            dfs(rowIndex, colIndex-1, visitSet, heights[rowIndex][colIndex])
            dfs(rowIndex, colIndex+1, visitSet, heights[rowIndex][colIndex])


        # Perform DFS starting for each element in the first and last row
        #   for pacific and atlantic respectively.
        #   Since we know that the first row can reach the pacific and last can reach the atlantic,
        #       any cell with an upward stream from them can reach those oceans as well.
        for c in range(COLS):
            dfs(0, c, pacificSet, heights[0][c])
            dfs(ROWS-1, c, atlanticSet, heights[ROWS-1][c])
        
        # Perform DFS on first and last column
        for r in range(ROWS):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, COLS-1, atlanticSet, heights[r][COLS-1])
        
        result = []
        # If an index is in both the pacific and atlantic sets, then append it to the result
        for pacSet in pacificSet:
            if pacSet in atlanticSet:
                result.append(pacSet)

        return result

# Time Complexity - O(m*n) => m:number of rows, n:number of columns
# Space Complexity - O(m*n)