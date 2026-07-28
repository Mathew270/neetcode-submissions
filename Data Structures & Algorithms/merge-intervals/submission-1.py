class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on starting pos
        intervals.sort(key=lambda x: x[0])
        res = []
        new = intervals[0]

        for i in range(1, len(intervals)):
            if new[1] < intervals[i][0]:
                res.append(new)
                new = intervals[i]
        
            else: # overlap
                new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]

        res.append(new)
        return res

        

