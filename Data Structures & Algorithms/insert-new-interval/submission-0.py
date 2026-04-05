class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            #if new_interval ka END is < i ka START
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new_interval ka START  is > i ka END
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # here just append i th interval and cpmare with next and else handles overlapping
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] # handles overlapping and puts 
                #updates it properly
        #after the for loop is done excuting we add the last interval
        #notice new interval is added only in on specific case in the top
        res.append(newInterval)
        return res