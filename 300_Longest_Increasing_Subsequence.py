from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Store the longestIncreasingSubsequence at each Index, 1 by default
        lisAtEachIndex = [1]*len(nums)
        # Loop from the end to the beginning
        for index in range(len(nums)-1, -1, -1):
            # searchIndex must be the every index after the current index
            for searchIndex in range(index+1, len(nums)):
                # If the current number is less than a following number, we have an increasing subsequence
                if nums[index] < nums[searchIndex]:
                    lisAtEachIndex[index] = max(lisAtEachIndex[index], 1+ lisAtEachIndex[searchIndex])
        return max(lisAtEachIndex)

# DP Solution: Starting from the end, store the longestIncreasingSubsequence possible at each index in an array. 
# Time - O(n^2)
# Space - O(n)


