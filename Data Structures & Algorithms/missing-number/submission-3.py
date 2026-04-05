class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            # res = len(nums) # res innitialized to len(nums) because for loop in index stops before len(nums) index 
            # for i in range(len(nums)):
            #     res += (i-nums[i]) #remaining will be the result 
            # return res
            # #or use binary XOR for completing
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i  ^ nums[i] #lettle confusing but but makes sense when u thing aboutit
        return res
        