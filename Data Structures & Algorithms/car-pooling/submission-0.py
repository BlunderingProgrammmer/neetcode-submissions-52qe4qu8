class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #not guarented soo sort
        trips.sort(key=lambda x:x[1])
        min_heap = [] # holds a pair of values [end ,num_of_passeners]
        # we care about who gets out first
        cur_pass = 0 

        for t in trips:
            num_of_passeners,start,end = t
            cur_pass += num_of_passeners 
            while min_heap and min_heap[0][0] <= start:
                cur_pass-=min_heap[0][1]
                heapq.heappop(min_heap)
            if cur_pass > capacity:
                return False
            heapq.heappush(min_heap,[end,num_of_passeners])

        return True


