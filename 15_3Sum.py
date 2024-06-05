from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    
    for i in range(len(nums)):
        # To prevent duplicate solutions
        if i!=0 and nums[i]==nums[i-1]:
            continue
        
        left, right = i+1, len(nums)-1
        while left<right:
            addedValue = nums[left]+nums[right]
            if addedValue == -nums[i]:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                # If there are duplicate values we move left to prevent duplicates
                # Duplicates can occur on the right too 
                #   but moving one will prevent duplicates because the sum value will  get mismatched
                while left<right and nums[left] == nums[left-1]:
                    left += 1
            # If sum of two values is greater than the complement we need, reduce right to decrease sum
            elif addedValue > -nums[i]:
                right -= 1
            else:
                left += 1

    return result


# Time Complexity - O(n^2) => O(n*logn) + O(n^2) (for sorting and iterations)
# Space Complexity - O(1)