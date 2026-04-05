class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select algo is annoying as fcuk so jsut use a god dam heap or sort here
        return heapq.nlargest(k,nums)[-1]