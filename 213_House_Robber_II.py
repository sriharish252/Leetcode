from typing import List

def maxRobLogic(nums: List[int]) -> int:
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

def rob(nums: List[int]) -> int:
    # Break the problem into two separate problems, one with the 1st house, another with the last house.
    #   This avoids worrying about the cycle. One edge case is: if the input is just 1 value, the slicing will send no value, so add that one input too as a factor in max calculation.
    return max(nums[0], maxRobLogic(nums[:-1]), maxRobLogic(nums[1:]))

print(rob([2,3,2]))

# Time Complexity - O(n)
# Space Complexity - O(1)