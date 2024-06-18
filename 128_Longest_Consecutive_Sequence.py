from typing import List

def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    maxLength = 0
    for n in numSet:
        # If previous not in numSet
        if (n-1) not in numSet:
            currentLength = 1
            # If next consecutive number is present, check if the further next consecutive number is present
            while (n+currentLength) in numSet:
                currentLength += 1
                maxLength = max(maxLength, currentLength)
    return maxLength

# Time Complexity - O(n)
# Space Complexity - O(n)