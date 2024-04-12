class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If k is greater than or equal to length(nums) take the reminder
        k %= len(nums)
        # Using Python slice operation to assign last k elements and then the first k elements
        nums[:] = nums[-k:] + nums[:-k]

# Time Complexity - O(n)
# Space Complexity - O(1)