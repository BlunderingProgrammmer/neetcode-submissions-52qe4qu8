class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #mistake i made i set sum +=i first then checked if sum >0
        # that means if first value is negative then it is always set to 0 then compared t0 res 
        #effectivly deleting the first value ahhhhhhhhhh stupid bug
        # res = nums[0]
        # sum = 0 
        # for i in nums:
        #     if sum < 0:
        #         sum = 0
        #     sum += i
        #     res = max(res,sum)

        # return res
        #using  a loop tactic
        res = nums[0]
        cursum = nums[0]

        for i in range(1,len(nums)):
            load = nums[i]
            cursum = max(load,cursum+load)
            res = max(res,cursum)
        return res