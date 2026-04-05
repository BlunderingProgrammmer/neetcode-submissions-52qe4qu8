class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #length check
        counts , countt = {}, {}
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i],0) 
            countt[t[i]] = 1 + countt.get(t[i],0) #create hashmap using get for def value

        for char in counts:
            if counts[char] != countt.get(char,0): #use get for def value compare count value 
                return False
        return True