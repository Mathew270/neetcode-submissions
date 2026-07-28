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
        # keep track of earliest end
        # if overlap:
            # rooms += 1
            # end = min(end, new-end)

        # if no overlap:
    

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        heap = [prev.end]
        heapq.heapify(heap)
        rooms = 1

        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]:
                rooms += 1
                heapq.heappush(heap, intervals[i].end)

            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)

        return rooms
        