class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        visit = set()
        count = 0

        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def bfs(v):
            q = deque()
            q.append(v)
            visit.add(v)

            while q:                                       
                cur = q.popleft()
                for nbr in adj[cur]:
                    if nbr not in visit:
                        visit.add(nbr)
                        q.append(nbr)

        for v in range(n):
            if v not in visit:
                bfs(v)
                count += 1

        return count

"""
def dfs(v):
            if v in visit:
                return
            visit.add(v)

            for nbr in adj[v]:
                dfs(nbr)
"""