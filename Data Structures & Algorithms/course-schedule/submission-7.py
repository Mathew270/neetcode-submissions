class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visiting = set()

        for nextt, pre in prerequisites:
            adj_list[nextt].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False

            if adj_list[crs] == []:   # used for quick way to check that all prerqs are done
                return True

            visiting.add(crs)

            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)   # it is no longer in current path
            adj_list[crs] = []     # we can take this course now  (update to []) for quick way to check
                                   # that all prereqs are done

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