class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        #above to create max_heap
        time = 0
        q = deque()
        #queue creation 
        while max_heap or q:
            time +=1 
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) #increament to decraemnet formmax heap 
                if cnt:
                    q.append([cnt,time+n]) # psuh to queue along  with target time
            if q and q[0][1] == time: #if curr time equal to target time push back to heap
                heapq.heappush(max_heap,q.popleft()[0])
        return time

