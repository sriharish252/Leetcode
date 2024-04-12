from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # List to store the minimum number of coins needed for each index value starting from 0 till amount
        minCoinsNeeded = [0] + [float("inf")]*amount
        
        # For each coin denomination
        for coin in coins:
            # Update every index from coin till end, since the ones before cannot be reduced
            for index in range(coin, amount+1): 
                # Min Coins needed is the min of existing value and 
                #   Number of coins needed for the amount Index - coin denomination + 1
                minCoinsNeeded[index] = min(minCoinsNeeded[index], minCoinsNeeded[index-coin] + 1)
        
        # If minimum coins are not computed for the target amount, update it as -1
        if minCoinsNeeded[amount] == float("inf"):
            minCoinsNeeded[amount] = -1
        return minCoinsNeeded[amount]

# Dynamic Programming solution
# Time - O(coins * amount)
# Space - O(amount)