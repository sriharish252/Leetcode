class Solution:
    def climbStairs(self, n: int) -> int:
        # (Number of ways to climb to n steps) = (Number of ways to climb to (n-1) steps) + (Number of ways to climb to (n-2) steps)
        #   Since we can jump 1 or 2 steps at a time.
        
        twoStepsBack = 1    # step 0, can be reached in 1 way
        oneStepBack = 1    # step 1, can be reached in 1 way
        
        for index in range(2, n+1):
            # Calculate ways to reach current step
            currentStep = twoStepsBack + oneStepBack
            # Update the values for next iteration
            twoStepsBack = oneStepBack
            oneStepBack = currentStep
        
        return oneStepBack

# Time Complexity - O(n)
# Space Complexity - O(1)