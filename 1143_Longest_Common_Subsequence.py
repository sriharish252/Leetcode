def longestCommonSubsequence(text1: str, text2: str) -> int:
    # len+1 because we add a dummy row and column of 0s in the beginning
    ROWS, COLS = len(text2)+1, len(text1)+1
    # Create a matrix to hold the max match of subsequence at every index
    #   Holds text1 as column headers and text2 as row headers
    dp = [[0 for j in range(COLS)] for i in range(ROWS)]
    for i in range(1, ROWS):
        for j in range(1, COLS):
            # If the characters match at that specific index, add 1 to the left top diagnol index
            if text2[i-1]==text1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            # Else take the max of left and above index
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[ROWS-1][COLS-1]

print(longestCommonSubsequence(text1 = "abcde", text2 = "acb"))

# Time - O(m*n) => m:length of text1, n:length of text2
# Space - O(m*n)
