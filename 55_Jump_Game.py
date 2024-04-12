from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        maxPossibleJump = 0
        while index<len(nums) and index<=maxPossibleJump:
            maxPossibleJump = max(maxPossibleJump, index+nums[index])
            index+=1
        return index==len(nums)

# Time - O(n)
# Space - O(1)