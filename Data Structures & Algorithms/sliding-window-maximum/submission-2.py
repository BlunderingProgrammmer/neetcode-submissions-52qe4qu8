class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r<len(nums):
            #store index in not value
            #while q not empty and top of q smaller than new r introduced
            #since its a monotonic q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # bounds check when window moves that its not still holding invalid value
            if l > q[0]: #max value always at the 0 position since monotonic que
                q.popleft()
            # chcek if window size is at leasst as big as k then only append to putput
            #after appending then only decrease window size from the left
            #after decreaing window size then increase from right 
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output