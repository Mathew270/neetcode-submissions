from collections import deque

class MaxQueue:
    def __init__(self):
        self.q = deque()        # Regular queue
        self.max_q = deque()    # Monotonic decreasing queue for max

    def push(self, x: int) -> None:
        self.q.append(x)
        # Maintain decreasing order in max_q
        while self.max_q and self.max_q[-1] < x:
            self.max_q.pop()
        self.max_q.append(x)

    def pop(self) -> int:
        if not self.q:
            return None
        val = self.q.popleft()
        if val == self.max_q[0]:
            self.max_q.popleft()
        return val

    def max(self) -> int:
        if not self.max_q:
            return None
        return self.max_q[0]

    def __len__(self):
        return len(self.q)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = MaxQueue()
        r = 0
        
        while(r < len(nums)):
            window.push(nums[r])

            if (len(window)) == k:
                res.append(window.max())
                window.pop()

            r += 1
        return res

