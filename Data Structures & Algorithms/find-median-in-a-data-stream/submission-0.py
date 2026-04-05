class MedianFinder:

    def __init__(self):
       
        # 2 heaps first and second ->MAX HEAP AND MIN HEAP RESPECT
       self.first , self.second = [],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first,-1 * num)
        if self.first and self.second and (-1 * self.first[0] > self.second[0]):
            val = -1 * heapq.heappop(self.first)
            heapq.heappush(self.second,val)
        # nowcheck if size is uneven on both
        if len(self.first) > len(self.second) + 1:
            val = -1 * heapq.heappop(self.first)
            heapq.heappush(self.second,val)
        if len(self.first)+1 < len(self.second):
            val = -1 *heapq.heappop(self.second)
            heapq.heappush(self.first,val)
    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -1 *self.first[0]
        if len(self.first) < len(self.second):
            return self.second[0]
        return (-1*self.first[0]+self.second[0])/2

        
        