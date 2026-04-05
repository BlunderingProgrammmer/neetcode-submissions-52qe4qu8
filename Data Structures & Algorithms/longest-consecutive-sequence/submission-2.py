class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) #fast lookup and no dupicates
        longest = 0

        for n in nums: #iterate through og nums
            if (n-1)  not in hashset:#check against hashset
                length = 0
                while (n+length) in hashset:#clever comp trick here adding length and increasing simonatanouly
                    length +=1
                longest = max(longest,length)
        return longest