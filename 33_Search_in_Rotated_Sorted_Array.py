from typing import List

def search(nums: List[int], target: int) -> int:
    # IDEA: We can identify if we the left to mid portion of the array is a sorted part
    #       of the array or not by comparing the mid and the left values, 
    #       using this info:
    #           If we are in a sorted portion:
    #               If the target is within that range, we move the 
    #                   left and right pointers like a binary search.
    #               If the target is less the beginning of array, 
    #                   then we search only the right portion like a subproblem.
    #           If we are not in a sorted portion:
    #               If target is less than mid, then search right portion.
    #               If target is greater than mid and greater than right, then search right portion.
    #               If target is greater than mid and less than rigth, then search left
    left, right = 0, len(nums)-1

    while left<=right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        # If left to mid portion of array is sorted
        if nums[left] <= nums[mid]:
            #If target is either >mid or (<mid and <left) then we search right portion
            if target > nums[mid] or target < nums[left]:
                left = mid+1
            else:
                right = mid -1
        # If left to mid portion of array is NOT sorted
        else:
            # If target is either <mid or (<mid and >right) then we search left portion
            if target < nums[mid] or target > nums[right]:
                right = mid -1
            else:
                left = mid +1
    return -1

print(search([4,5,6,7,0,1,2], 0))

# Time Complexity - O(log n)
# Space Complexity - O(1)