class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i : [] for i in range(numCourses)} 
        # map all courses not just ones that have pre req (prerequisites [])
        inDegree = [0] * numCourses
        q = deque()

        for course, pre in prerequisites:
            adj[pre].append(course)
            inDegree[course] += 1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            cur = q.popleft()
            res.append(cur)
            finished += 1
            for nbr in adj[cur]:
                inDegree[nbr] -= 1
                if inDegree[nbr] == 0:
                    q.append(nbr)

        return res if finished == numCourses else []

        