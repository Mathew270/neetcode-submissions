class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visit = set()

        for nextt, pre in prerequisites:
            adj_list[nextt].append(pre)

        def dfs(crs):
            if crs in visit:
                return False

            if adj_list[crs] == []:
                return True

            visit.add(crs)

            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            adj_list[crs] = []

            return True

        for crs in list(adj_list.keys()):
            if not dfs(crs):
                return False
        
        return True
"""
q = deque()
            q.append(pre)
            visit.add(pre)

            while q:
                cur = q.popleft()
                for nbr in adj_list[cur]:
                    if nbr in visit:
                        return True
                    visit.add(nbr)
                    q.append(nbr)
"""