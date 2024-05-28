def countSubstrings(self, s: str) -> int:
    result = 0
    for i in range(len(s)):
        # Odd len substring case
        left, right = i, i
        def checkAndUpdatePalindrome(left, right, result):
            # If it is a palindrome, increment the result and move pointers to left and right
            while left>=0 and right<len(s) and s[left]==s[right]:
                result += 1
                left -= 1
                right += 1
            return result
        result = checkAndUpdatePalindrome(left, right, result)

        # Even len substring case
        left, right = i, i+1
        result = checkAndUpdatePalindrome(left, right, result)
    return result

# Time Complexity - O(n^2)
# Space Complexity - O(1)