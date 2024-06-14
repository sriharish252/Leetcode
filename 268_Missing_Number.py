from typing import List

def missingNumber(self, nums: List[int]) -> int:
    # IDEA: XOR operation between all  numbers in list and all numbers in range
    #       This elimates numbers with same values, so missing number remains
    numbers = 0
    for i in range(1,len(nums)+1):
        numbers ^= i
    for n in nums:
        numbers = numbers^n
    return numbers

# Time Complexity - O(n)
# Space Complexity - O(1)