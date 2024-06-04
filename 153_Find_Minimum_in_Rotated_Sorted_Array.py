from typing import List

def findMin(nums: List[int]) -> int:
    # IDEA: Binary Search
    left, right = 0, len(nums)-1
    while left<right:
        mid = (left+right) // 2
        if nums[mid]<nums[right]:
            # Not (mid-1) because mid can be min value
            right = mid
        else:
            left = mid+1
    return nums[left]

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
print(findMin([2,1]))
print(findMin([5,1,2,3,4]))
print(findMin([3,1,2]))
print(findMin([1,2,3]))
print(findMin([1,2,3,4]))

# Time Complexity - O(log n)
# Space Complexity - O(1)