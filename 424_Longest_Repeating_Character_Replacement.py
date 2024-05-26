
def characterReplacement(s: str, k: int) -> int:
    # Idea: Sliding Window. Store count of each alphabet in the selected string.
    #       If the string is invalid, move left pointer by 1 index and check.
    #       As long as string is valid, move right pointer to the right.
    countDict = {}
    maxLen = 0
    left = 0

    for right in range(len(s)):
        # Increments the count of the alphabet by 1
        countDict[s[right]] = 1 + countDict.get(s[right], 0)
        
        # If (length of Current string - countOfMostFreqAlphabet) > k, then invalid
        if ((right - left + 1) - max(countDict.values())) > k:
            # Reduce the count of the left pointer alphabet since we move the left
            countDict[s[left]] -= 1
            left += 1
        maxLen = max(maxLen, (right - left + 1))
    return maxLen

print(characterReplacement("ABAB", 2))
print(characterReplacement("ABAB", 1))

# Time - O(n) # Actually O(26*n)
# Space - O(1) # Actually O(26)

# Can be optimized by using a maxFrequence variable,
#   which avoids checking the max of every value in dictionary.
#   Time becomes O(n) instead of O(26*n)