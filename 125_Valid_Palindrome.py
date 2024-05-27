def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    left, right = 0, len(s)-1
    while left<=right:
        if s[left]!=s[right]:
            return False
        left += 1
        right -= 1
    return True

# Time Complexity - O(n)
# Space Complexity - O(1)