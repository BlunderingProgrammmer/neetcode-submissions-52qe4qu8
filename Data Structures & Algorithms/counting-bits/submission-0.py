class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)  #intitialize a array with def value as 0 of length n+1 due to 0 indexing
        offset = 1 # set default offset as 1 ,offset is basically 2**(0,1,2,3,4,....) most significant countBits
        for i in range(1,n+1): #iterate from 1 to n+1 since def value is set to 0
            if offset * 2 == i:# check if new offset can be calculated
                offset = i
            dp[i] = 1 + dp[i - offset] # no oof 1 at i index = 1 (most significant bit )+ no of 1 at i - offset
        return dp# using prev result to get present result dp :) 
