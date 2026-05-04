class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #not guarented soo sort
        trips.sort(key=lambda x:x[1])
        min_heap = [] # holds a pair of values [end ,num_of_passeners]
        # we care about who gets out first
        cur_pass = 0 

        for t in trips:
            #get variables cuz trip just started
            num_of_passeners,start,end = t
            cur_pass += num_of_passeners 
            #check when the trip started did the any other trip  end  
            while min_heap and min_heap[0][0] <= start:
                cur_pass-=min_heap[0][1]
                heapq.heappop(min_heap)
            #check against capacity
            if cur_pass > capacity:
                return False
            #push current trip into the trip 
            heapq.heappush(min_heap,[end,num_of_passeners])

        return True


