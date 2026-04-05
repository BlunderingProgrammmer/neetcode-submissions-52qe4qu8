class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_hash = Counter(tasks)#just creates a hashmap for us no need to write code
        max_heap = [-cnt for cnt in freq_hash.values()]
        heapq.heapify(max_heap)
        q = deque() #[cnt,time when that task is avialable]
        time = 0
        #intialise all variebles -q is use keep track of task availablity
        while max_heap or q:
            time +=1
            if max_heap:
                cnt = 1+heapq.heappop(max_heap)#since while loop starts with time increament we also add to time in count(since time is neg we add)
                if cnt:#if cnt becomes 0 -task is already precessed so no need to add to q
                    q.append([cnt,time+n])
            if q and q[0][1] == time:#check if avia time == current time-if yes add to heap
                heapq.heappush(max_heap,q.popleft()[0])
        return time 