class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                #perform a safety bounds check
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: #most imp part think this section through
                    dp[i] = dp[i+len(word)]
                if dp[i]: #if dp of [i returns true then break out off comparission btw words in words dict]
                    break
        return dp[0] #bottem up stays in 0 res