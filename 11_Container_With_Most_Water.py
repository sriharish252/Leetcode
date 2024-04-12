from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        maxHeight = 0
        i = 0
        j = len(height)-1
        while i<len(height) and j>=0:
            if min(height[i], height[j]) > maxHeight:
                maxHeight = min(height[i], height[j])
                maxArea = max(maxHeight*(j-i), maxArea)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxArea

# Two pointer solution
# Time - O(n)
# Space - O(1)