class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #use prefix and postfix array in same output array with def 1
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):#-1 on stop because range in py does not include itself
            res[i] *= postfix
            postfix *= nums[i]
        return res        