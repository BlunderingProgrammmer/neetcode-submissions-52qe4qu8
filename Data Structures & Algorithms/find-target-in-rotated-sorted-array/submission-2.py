class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0 ,len(nums)-1
        while l<=r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            #check if in leftsorted portion or right sorted portion of sorted array
            if nums[l] <= nums[mid]:#left_sorted portion if true
                if target > nums[mid] or target < nums[l]:#check mid as well
                    l = mid + 1
                else:
                    r = mid - 1
            else:#write conditions of right sorted array
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else :
                    l = mid + 1
        return -1