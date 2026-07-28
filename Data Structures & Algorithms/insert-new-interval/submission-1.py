class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if end of curr-interval is less than start of newInterval
            # we can safely add curr-interval to res
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # if end of newInterval is less than start of curr-interval
            # result = (already added intervals) + newInterval + rest of intervals
            elif newInterval[1] < intervals[i][0]:
                return res + [newInterval] +  intervals[i:]

            else: # overlap
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        # if we reach here means we newInterval is yet to be added
        # this means elif part was never executed
        res.append(newInterval)
        return res