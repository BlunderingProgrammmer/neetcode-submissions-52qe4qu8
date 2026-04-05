class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0# intialize at the first
        while r<len(nums)-1:# while r is not at the last number
            fartest_jump = 0 
            for i in range(l,r+1):
                fartest_jump = max(fartest_jump,i+nums[i])
            l = r +1
            r = fartest_jump
            res+=1#finshing the for loop means one unit of jump or one session of bfs

        return res