from typing import List

def maxProfit(self, prices: List[int]) -> int:
    # Two Pointer Solution
    left, right = 0, 0
    maxDifference = 0
    for right in range(len(prices)):
        if prices[left]<prices[right]:
            maxDifference = max(maxDifference, prices[right]-prices[left])
        else:
            # If price[right] is less than left, it means a new min price is found
            #   So update left to that position
            left=right
    return maxDifference

# Time Complexity - O(n)
# Space Complexity - O(1)