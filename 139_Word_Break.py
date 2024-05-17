from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False]*(len(s)+1)
    # Base Case: End of String (a.k.a. empty string) is True
    dp[len(s)] = True

    # Iterate from last index to the beginning
    for currentStartingIndex in range (len(s)-1, -1, -1):
        # Loop through every word in Dictionary to check if it matches
        for word in wordDict:
            # If dictionary word is less than or equal to substring length and substring is exact match of the dictionary word
            if len(word) <= (len(s)-currentStartingIndex) and s[currentStartingIndex: currentStartingIndex+len(word)] == word:
                # Then word reach is determined by the end of substring's next starting index
                dp[currentStartingIndex] = dp[currentStartingIndex+len(word)]
            
            # If currentStartingIndex can be reached, no need to check alternative reach
            if dp[currentStartingIndex] == True:
                break
    return dp[0]

print(wordBreak("leetcode", ["leet","code"]))

# Time Complexity - O(n^2*m) => n=length(s), m=length(wordDict)
# Space Complexity - O(n)