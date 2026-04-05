class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        #init the def value for dp
        #base case:
        dp[0] = 0
        for amt in range(1,amount+1):
            for coin in coins:
                left_over = amt - coin
                if left_over >=0:
                    dp[amt] = min(dp[amt],1+dp[left_over])
        return dp[amount] if dp[amount] != amount+1 else -1

        #read this again for clarity
        