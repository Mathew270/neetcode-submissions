from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
# key intuition:
# the task (letter eg. "A") that appears the most number of times
# should be executed first, so as to minimize the number of idle's
# since other tasks can be put in between one task of A and another A
# if we leave the A's to later then we wont have tasks to place 
# in between 2 A's meaning we increase no. of cycles by placing idles

# the way we keep track of which has the most count is to use a max heap
# and we use a queue (containing (count, time) )
# count: tells us count of task (stuff we still need to reduce to 0)
# time: to check if task at top of the q has time == curr_time
#       so we can pop of the task

# in the end return time

        time = 0
        count = {}
        q = deque()

        max_heap = []

        for c in tasks:   # get count of chars
            count[c] = count.get(c, 0) + 1

        for c in count:
            max_heap.append(-count[c])

        heapq.heapify(max_heap)    # create max heap (negated counts)

        while max_heap or q: # while there are elements in heap or q
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)   # heappop gives -ve value so + 1 to reduce it
                if cnt: # if count not 0
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
            










