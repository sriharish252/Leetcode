from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
    rowSet = [set() for _ in range(9)]
    colSet = [set() for _ in range(9)]
    subSet = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            # Check each Row
            if num in rowSet[i]:
                return False
            rowSet[i].add(num)

            # Check each Column
            if num in colSet[j]:
                return False
            colSet[j].add(num)

            # Check each subBox, there are 9 sets, each representing each subbox
            #   they are navigated using the below formula
            subBoxIndex = (i//3)*3 + (j//3)
            if num in subSet[subBoxIndex]:
                return False
            subSet[subBoxIndex].add(num)
    return True

# Time Complexity - O(m*n) => m:number of rows, n:number of columns
# Space Complexity - O(m*n)

print(isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))