"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #so your are iterating through a list of objects    
        #sort solutions 
        #first create a list of start and end objects
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        max_count,count = 0,0

        #create two trailing pointers
        s,e = 0,0

        #now iterate
        while s < len(start):#only need to iterate till start array items end since iterating through 
        #end array items only decreases the count not increase it and we need the max count
            if start[s] < end[e]:
                count+=1
                max_count = max(count,max_count)
                s+=1
            else:#start[s] >= end[e]
                e+=1
                count -=1

        return max_count

