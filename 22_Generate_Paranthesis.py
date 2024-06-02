from typing import List

def generateParenthesis(self, n: int) -> List[str]:
    # Stores paranthesis value each recursive backtrack state
    paranthesisList = []
    result = []

    # Recursive function to generate all valid combinations
    def backtrack(openCount, closedCount):
        # If openParanthesisCount = closed = our target 'n', we found a valid combination, so return
        if openCount == closedCount ==n:
            result.append("".join(paranthesisList))
            return
        
        # If count of existing Open paranthesis is less than n, we can add more
        if openCount < n:
            paranthesisList.append("(")
            backtrack(openCount+1, closedCount)
            # Remove the added new paranthesis once that path is done
            paranthesisList.pop()
        
        # Only if count of existing Closed paranthesis is less than Open we can make a valid string
        if closedCount < openCount:
            paranthesisList.append(")")
            backtrack(openCount, closedCount+1)
            paranthesisList.pop()
    
    backtrack(0, 0)
    return result

# Time Complexity - O(2^2n)
# Space Complexity - O(n)