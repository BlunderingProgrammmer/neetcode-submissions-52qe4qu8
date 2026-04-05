class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed_1 , robbed_2 = 0,0
        #[robbed_1,robbed_2,n,n+1,n+2]
        for n in nums:
            temp = max(robbed_1+n,robbed_2) #maximum between i and 1+2 ,just i+1
            robbed_1 = robbed_2 #moving the variables
            robbed_2 = temp
        return robbed_2