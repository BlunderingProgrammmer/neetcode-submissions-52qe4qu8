class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.house_robber_1(nums[1:]),self.house_robber_1(nums[:len(nums)-1]))
        #nums[0] handles a edge case where onmy one value is given         
        
        
    def house_robber_1(self,nums):
        robbed_1 , robbed_2 = 0,0
        #[robbed_1,robbed_2,n,n+1,n+2]
        for n in nums:
            new_robbery = max(robbed_1+n,robbed_2) #maximum between i and 1+2 ,just i+1
            robbed_1 = robbed_2 #moving the variables
            robbed_2 = new_robbery
        return robbed_2