"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #heap Solution
        #step_1 sort on the basis of start time
        intervals.sort(key=lambda x :x.start)#using an annonimos function as a key
        #initialize  min heap
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval.end)
        return len(min_heap)
