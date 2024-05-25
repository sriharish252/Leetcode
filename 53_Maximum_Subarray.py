from typing import List

def maxSubArray(nums: List[int]) -> int:
    # Idea: Consider a prefix sum type calculation where if the sum is -ve,
    #           we move the start of the subarray to the next index,
    #            by resetting the sum to 0 and starting again. This way, we can get the max possible.
    #       Kinda like sliding window.
    maxSum = -float("inf")
    currentSum = 0
    for index in range(0, len(nums)):
        currentSum += nums[index]
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum<0:
            currentSum = 0
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Time Complexity - O(n)
# Space Complexity - O(1)