from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    nextIndexCost, secondNextIndexCost = 0, 0
    for num in cost[::-1]:
        curIndexCost = min(num+nextIndexCost, num+secondNextIndexCost)
        secondNextIndexCost = nextIndexCost
        nextIndexCost = curIndexCost
    return min(nextIndexCost, secondNextIndexCost)


print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

# Time Complexity - O(n)
# Space Complexity - O(1)