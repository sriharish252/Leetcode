from typing import List

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []
    
    def backtrack(index, currentPath, currentSum):
        if currentSum == target:
            # Creating a copy of currentPath, since currentPath List is used downstream
            #   and we shouldn't modify the list stored in result. So we create a new List instance.
            result.append(currentPath.copy())
            return
        if index>=len(candidates) or currentSum > target:
            return
        
        # Branch 1: Selecting the current Index
        currentPath.append(candidates[index])
        backtrack(index, currentPath, currentSum+candidates[index])
        
        # Branch 2: Skipping the current Index
        currentPath.pop()
        backtrack(index+1, currentPath, currentSum)

    backtrack(0, [], 0)
    return result

# Time Complexity - O(2^n)  => Approximately two choices at each index
# Space Complexity - O(n)