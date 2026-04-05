class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] #set to an arbritaryy value in the given list
        l ,r = 0 ,len(nums) -1
        while l <= r:
            mid = (l+r) // 2
            if nums[l] < nums[r]:
                res = min(res,nums[l]) #check if in sorted array or something then 
                break
            res = min(res,nums[mid])#always consider mid as canditate for min
            if nums[mid] >= nums[l]:#means we are in the left sorted array
                l = mid + 1
            else:
                r = mid -1
        return res