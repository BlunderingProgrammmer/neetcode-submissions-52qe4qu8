class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #overlapping merge rule:
        #if the start time is greater or equal to the starttime of another and
        #end time is smaller or equal toend time of another the mergable 
        #BUT
        #once sorted
        #rule -> start time of i is less than or equal to end time  then they can be merged
        intervals.sort(key=lambda x:x[0])
        output = []
        output.append(intervals[0])

        for start,end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                #then can be merged
                output[-1][1] = end if last_end < end else last_end

            else:
                output.append([start,end])
        return output



