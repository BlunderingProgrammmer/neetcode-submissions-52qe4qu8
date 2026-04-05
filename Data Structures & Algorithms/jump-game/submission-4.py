class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_last_index = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal_last_index:
                goal_last_index = i
        return True if goal_last_index  == 0 else False