class Solution:
    def numDecodings(self, s: str) -> int:
        #base hash map - { sub problem results is stored}
        dp = {len(s) : 1} #number_string length-> no of ways can be decoded
        #base case where the entire len by def is one
        def dfs(i):
            if i in dp:
                return dp[i] #base check and edge case check
            if s[i] == '0':
                return 0
            #two branches in decidion include or not include
            #store first in res and then check for next validity
            res = dfs(i+1) 
            if (i+1 < len(s) and 
                (s[i] == '1' or 
                s[i] == '2' and s[i+1] in '0123456')):
                res += dfs(i+2)
            dp[i] = res#cache it
            return res #return final res after all calls
        return dfs(0)
