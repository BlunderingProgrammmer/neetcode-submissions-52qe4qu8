class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:#i>0 condition is to check if i is stilll on the first element ..if it is the next condition will fail 
                continue
            l,r = i+1,len(nums)-1 #l and right start always after intial i 
            while l < r:
                if v + nums[l] + nums[r] > 0:
                    r-=1
                elif v + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    r-=1 #increament both l and r to see other sol exist for same intial value
                    while l<r and nums[l] == nums[l-1]: #dup check for the pointer similar to above ka i check this time its for l and r pointers
                        l+=1

        return res