class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        visit = set()  # stores indicies that we added to q, so we dont add repeat
        q.append((0, nums[0]))
        visit.add(0)
        jumps = 0

        while q:
            for i in range(len(q)):
                curr_idx, dist = q.popleft()

                if curr_idx == n - 1:
                    return jumps

                if dist == 0:
                    continue

                for i in range(1, min(n - 1, curr_idx + dist) + 1):
                    new_idx = i

                    if new_idx not in visit:
                        q.append((new_idx, nums[new_idx]))
                        visit.add(new_idx)

            jumps += 1

        return -1