from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

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
            
# key intuition: 
# 1) (purpose of heap)

# the task (letter eg. "A") that appears the most number of times
# should be executed first, so as to minimize the number of idle's
# since other tasks can be put in between one task of A and another A
# if we leave the A's to later then we wont have tasks to place 
# in between 2 A's meaning we increase no. of cycles by placing idles

# so our aim is to always retrieve and execute the task with the max count everytime
# hence we use a heap

# when we execute a task we reduce count by 1 and then add it back to heap
# but since python doesnt allow max_heap we use min_heap with -ve values

# to decrease a value we actually have to + 1 to popped value then push to heap

"""
---------------------------------------------------------------------
2) purpose of queue

but we cannot just get the max from the heap everytime,
we can only execute (pop a task) from the heap once we have waited 
n cycles. 

so thats why we use a queue (the queue is to validate the addition of the task to our heap)
we pop from the queue if the (top of the q's time) == current time

we append every task to a queue after popping from the max heap if the task's count
is still not 0

we append (cnt, curr_time + n) because now
when we check (top of q's time) == curr time. we then add (top of q) to the heap
------------------------------------------------------------------
3) why we appendd [cnt, (time + n)] to queue

(time + n):

eq. n = 3
we pop A at time = 1
the next time we can execute A is 
A - - - A (at time == 5)
so when we reach (curr_time + n): == (the time we append in the queue)

we take the element from q and put it in the heap
so now in the next time (time == 5)
we are indeed allowed to execute that task

(cnt):

the reason we append cnt is because this is the value we are going to add to 
the heap when the time condition is met 

(so the time + n is used to validate wether we can append to heap
and cnt is what we are actually adding to the heap)

this is how the algorithm works
-----------------------------------------------------------------
4) why a queue works here

the reason we use a queue is because we are guaranteed that the task 1st appended
will have a smaller time than anything that comes after it

because we always append (time + n) to the q. 
time is always increasing and n stays the same
---------------------------------------------------------------------
5) in case of no elements in heap

in the case of no elements in the heap:
we just take the top element in the queue and jump to that time
set time == q[0][1]

then pop from q
"""






