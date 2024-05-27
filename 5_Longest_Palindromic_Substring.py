def longestPalindrome(self, s: str) -> str:
    currentLongestPalin = ""
    for i in range(len(s)):
        # Odd len substring case
        left, right = i, i
        def checkAndUpdatePalindrome(left, right, currentLongestPalin):
            while left>=0 and right<len(s) and s[left]==s[right]:
                if len(s[left:right+1]) > len(currentLongestPalin):
                    currentLongestPalin = s[left:right+1]
                left -= 1
                right += 1
            return currentLongestPalin
        currentLongestPalin = checkAndUpdatePalindrome(left, right, currentLongestPalin)

        # Even len substring case
        left, right = i, i+1
        currentLongestPalin = checkAndUpdatePalindrome(left, right, currentLongestPalin)

    return currentLongestPalin

# Time Complexity - O(n^2)
# Space Complexity - O(n)