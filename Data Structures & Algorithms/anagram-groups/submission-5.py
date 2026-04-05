from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #default calue for a key:value pair is a empty list since speciafied in code
        for s in strs:
            count = [0] * 26 #for each word create a seperate freq array
            for c in s:
                count[ord(c) - ord('a')] +=1  # 0 if does not exist 
            res[tuple(count)].append(s)#list cant be key so tuple since default is list u can append to it using append()
        return list(res.values())