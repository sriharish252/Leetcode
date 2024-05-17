from typing import List

def rob(nums: List[int]) -> int:
    # Two variable to keep track of max possible amount when robbed house1 and house2 resp.
    robHouse1, robHouse2 = 0, 0

    for num in nums:
        # The max amount at each index is (current house + max at two indices before(i.e., house1)) or (max at one index before(i.e., house2))
        maxAtcurrentIndex = max(num+robHouse1, robHouse2)
        # Move the variables right by one index as we move to the next house
        robHouse1 = robHouse2
        robHouse2 = maxAtcurrentIndex
    # Return the max amount at the last index which is robHouse2
    return robHouse2

print(rob([1,2,3,1]))

# Time Complexity - O(n)
# Space Complexity - O(1)