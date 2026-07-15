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

        """
        check prev qn for post order dfs way to topo sort

------------------------------------------------------------------------------------------------
        how Kahn algo using indegrees works:

        the way we know that No cycle is detected is by checking if all nodes
        IN THE ADJ_LIST ARE VISITED (all nodes in the graph we create)

        if theres a cycle (we know not all nodes will be visited) why?
        
        this is because we only append to the q 
        when a node has indegree 0 (finished all pre reqs) (incoming edges)
        when we visit a node while iterating through parent we do 

        inDegree[nbr] -= 1   (we have traversed this incmoing edge) (so reduce indegree by 1)


        nodes in a cycle will never get appened to q since
        the nodes are mutually dependant they will never hit indegree 0

-------------------------------------------------------------------------------------------------------
        when initializing adjList 
        have in the back of ur mind whether ur adding all possible nodes
        or just nodes in the edge list (some nodes could be excluded)

        this point is more relevant for course schedule

        when we check if (finished == numCourses)

        we do this 
        adj = {i : [] for i in range(numCourses)} 

        rather than just this
        for course, pre in prerequisites:
            adj[pre].append(course)

        if we only do the above we might miss out on some courses that dont
        have any prereqs
        hence not in prereq array

        since 
        the way we know that No cycle is detected is by checking if all nodes
        IN THE ADJ_LIST ARE VISITED (all nodes in the graph we create)

        if we wrongly do 
        (finished == numCourses)

        this is an incorrect check since the graph we created never actually 
        included courses/ nodes not in prereq array

        so be careful when creating adj_list and doing final check
        """

        