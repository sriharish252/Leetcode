from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    # Stores indices of the path taken, to avoid selecting the same index twice
    path = set()

    def dfs(currentRow: int, currentColumn: int, wordIndex: int) -> bool:
        # If reached the end of word, found the word, so return true
        if wordIndex == len(word):
            return True
        
        # If index is out of bounds or 
        #   current letter is not in the current Index or 
        #   currentIndex already seleceted (exists in path set)
        if (currentRow < 0 or currentRow >= len(board) or 
            currentColumn < 0 or currentColumn >= len(board[0]) or 
            board[currentRow][currentColumn] != word[wordIndex] or 
            (currentRow, currentColumn) in path):
            return False
        
        # Add current index to path
        path.add((currentRow, currentColumn))
        
        # Traverse through adjacent indices, to see if any of it is true
        result = (dfs(currentRow, currentColumn+1, wordIndex+1) or 
                  dfs(currentRow, currentColumn-1, wordIndex+1) or 
                  dfs(currentRow-1, currentColumn, wordIndex+1) or 
                  dfs(currentRow+1, currentColumn, wordIndex+1))
        
        # Remove current index from path to allow backtracking
        path.remove((currentRow, currentColumn))
        return result

    # Perform DFS from every index in the board as the starting position till word is found
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

# Time Complexity - O(rows* columns* 4^len(word))
# Space Complexity - O(len(word))