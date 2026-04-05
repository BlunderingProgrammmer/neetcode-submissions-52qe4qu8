class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in premap:
                return [premap[diff],i]
            premap[v] = i
        return 