class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in char_set: #check if dup exist in set since set cant have dups
                char_set.remove(s[l])#remove said dup
                l+=1#increament pointer
            char_set.add(s[r])
            res = max(res,r-l+1)
        return res
            