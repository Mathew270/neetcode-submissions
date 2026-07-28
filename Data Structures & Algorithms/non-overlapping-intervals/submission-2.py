class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        ending = prev[1]
        removed = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < ending: # overlap (start of next is less than end of prev)
                removed += 1
                ending = min(ending, intervals[i][1])  # end = min(end1, end2) (since we are removing one with larger end)

            else:     # if not removing, ending = end of new interval
                ending = intervals[i][1]

        return removed