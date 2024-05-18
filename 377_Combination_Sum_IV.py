from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    # Store the number of possible combinations for each target value.
    dp = [0]*(target+1)
    # Base case: For target=0, number of possible ways= 1 (Select nothing)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            # If num<i then (i-num) is negative, there are no negative nums
            if i >= num:
                dp[i] += dp[i-num]
    return dp[target]

print(combinationSum4([1,2,3], 4))

# Time Complexity - O(target*len(nums))
# Space Complexity - O(target)