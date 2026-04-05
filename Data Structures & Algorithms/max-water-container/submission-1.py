class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l, r = 0 ,len(heights)-1 #two pointer sol
        while l < r :
            area = (r-l) * min(heights[l],heights[r]) #width = r index - l index value
            res = max(res,area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r-=1
        return res