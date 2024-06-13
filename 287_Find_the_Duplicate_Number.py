from typing import List

def findDuplicate(self, nums: List[int]) -> int:
    # Idea: Consider this as a Linked List question.
    #       Each value is the index of the next node, 
    #           starting from first index.

    # Setting slow and fast to the first index
    slow, fast = 0, 0

    # Identify the cycle detection node
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Identify the cycle's starting node using Floyd's Cycle Algorithm
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

# Time Complexity - O(n)
# Space Complexity - O(1)