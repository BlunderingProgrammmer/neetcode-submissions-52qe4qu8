class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in nums:
                cur_length = 0 
                while (i+cur_length) in nums:
                    cur_length += 1
                longest = max(cur_length,longest)
        return longest