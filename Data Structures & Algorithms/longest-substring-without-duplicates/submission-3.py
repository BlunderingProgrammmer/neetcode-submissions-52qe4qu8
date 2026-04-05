class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #first create a charecter set
        charset = set() #cant have dups soo we use to compare and o(1) lookup
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charset: #compare with our set to see alread existing
                charset.remove(s[l])#remove from left 
                l+=1 #increment left pointer
            charset.add(s[r]) #add the new pointer we found
            res = max(res,r-l+1)
        return res
