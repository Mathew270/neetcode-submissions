from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()

        def dfs(node):
            if node in path:  # cycle detected
                return False
            if node in visited:  # already processed
                return True
            
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visited.add(node)
            return True  # all children processed safely

        for course in range(numCourses):
            if not dfs(course):
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