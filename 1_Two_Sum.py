from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Instead of putting every value in a hashMap, 
    #   we can do just 1 pass through the list and update the hashMap as we go

    # Store value: index
    hashMap = {}

    for i, n in enumerate(nums):
        difference = target-n
        # If difference is found in hashMap return indices
        if difference in hashMap:
            return [i, hashMap[difference]]
        
        # Store value and corresponding index in hashMap
        hashMap[n] = i
    
    # Since the question says there definitely exists a solution, this return is just a placeholder
    return

print(twoSum(nums = [2,7,11,15], target = 9))

# Time Complexity - O(n) => n: length of nums list
# Space Complexity - O(n)