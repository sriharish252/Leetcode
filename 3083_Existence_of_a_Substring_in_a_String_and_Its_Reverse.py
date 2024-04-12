class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for index in range(len(s)-1):
            # Check if substring of length 2 is present in reverse of string
            if s[index: index+2] in s[::-1]:
                return True
        return False

# Time Complexity: O(n^2) -> n for For loop and another n for the in operator
# Space Complexity: O(1)


# Alternate Solution:

from itertools import pairwise
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversedPairSet = {(a, b) for a, b in pairwise(s[::-1])}
        return any((a, b) in reversedPairSet for a, b in pairwise(s))

# Time Complexity: Θ(n), O(n^2) 
#                   -> n for For loop, 
#                      n for "in" operator in Set (Average case is Θ(1))
# Space Complexity: O(|Σ|^2), where Σ is the character set, i.e., 26 in this case
#                   -> since only unique values are stored, (26^2) combinations are only possible