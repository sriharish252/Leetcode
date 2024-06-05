from typing import List

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1
    while left<right:
        addedValue = numbers[left]+numbers[right]
        if addedValue == target:
            return [left+1, right+1]
        elif addedValue > target:
            right -= 1
        else:
            left += 1

# Time Complexity - O(n)
# Space Complexity - O(1)