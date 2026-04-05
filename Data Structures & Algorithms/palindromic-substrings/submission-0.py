class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #for odd length count_palindrone
            l = r = i
            res += self.count_palindrone(s,l,r)
            l = i
            r = i+1
            res += self.count_palindrone(s,l,r)
        return res

    def count_palindrone(self,s,l,r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
        return res