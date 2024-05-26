def lengthOfLongestSubstring(s: str) -> int:
    # Idea: Sliding Window. 
    #       Move the left pointer to the immediate right index of the duplicate alphabet's last seen position.
    hashMap = {}
    maxLen = 0
    left, right = 0, 0
    while left < len(s) and right < len(s):
        if s[right] not in hashMap:
            hashMap[s[right]] = right
        else:
            # If left was already moved further, we shouldn't move it back hence use max() here.
            left = max(left, hashMap[s[right]] + 1)
            hashMap[s[right]] = right
        # Update maxLen
        maxLen = max(maxLen, (right - left + 1))
        right += 1
    return maxLen

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("abc"))

# Time - O(n)
# Space - O(n)