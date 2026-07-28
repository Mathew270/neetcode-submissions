"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:\
        # sort by start
        # store end times in a heap
        # if overlap (curr-start < top-of-heap = (min end time)):
            # rooms += 1
            # push new-end-time to heap

        # if no overlap:
            # pop best end time
            # push new end time (room of old meeting replaced by this meeting, hence, new end)
    

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        heap = [prev.end]
        rooms = 1

        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]:
                rooms += 1
                heapq.heappush(heap, intervals[i].end)

            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)

        return rooms
        