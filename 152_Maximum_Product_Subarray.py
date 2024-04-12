from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # To store max product value
        maxProd = nums[0]
        # To store min product value, since can become max value if multiplied with a -ve number
        minProd = nums[0]
        overallMax = nums[0]
        
        for index in range(1, len(nums)):
            num = nums[index]
            
            # maxProd possible is either the new number, or it multiplied by maxProd or minProd(if it's negative)
            # It is stored in currentMaxProd, since we need the previous maxProd for computation of minProd
            currentMaxProd = max(num, num*maxProd, num*minProd)
            
            # Similarly, update minProd since it could become maxProd in future iterations
            minProd = min(num, num*minProd, num*maxProd)
            
            # Update the found maxProd value
            maxProd = currentMaxProd
            # Compares the current max product with the overall max product found in previous subarrays
            overallMax = max(maxProd, overallMax)
        return overallMax

# Time - O(n)
# Space - O(1)