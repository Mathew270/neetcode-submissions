class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create adj_list
        adj_list = {i : [] for i in range(numCourses)}  
        # initialize for every course not just ones that have prereq (in prereq [])

        visited = set()
        onPath = set()

        for course, pre in prerequisites:
            adj_list[pre].append(course)  # prereq -> course

        def dfs(pre):
            if pre in onPath:
                return False       # cycle is found (visiting a node alr on path)
            if pre in visited:
                return True        # this means no cycle from this node
            
            onPath.add(pre)            # add node to path
            for nbr in adj_list[pre]:
                if not dfs(nbr):
                    return False     # return False as soon as cycle is encountered
            
            onPath.remove(pre)
            visited.add(pre)
            return True             # return True after all nbrs have been processed
            

        # check if cycle exists (start from every node incase more than 1 connected comp)
        for pre in range(numCourses):
            if not dfs(pre):   
                return False

        return True


        # once we traverse through all nbrs we process(node) -> add to visited
        # if we visit something in our current path -> cycle
        
        # basic post order dfs:
        #   base cases:
        
        #   path.add(node)
        #   for each nbr:
        #      if not in path:
        #           dfs(nbr)
        #   path.remove(node)
        #   process(node)
        

        """
        what we're doing here is similar but 

        if we see a nbr in our curr path
        we return false

        if our nbr is in visited we return True

        and our process(node) just adding to visited

        once we successfully go through a nodes nbrs, 
        we remove node from path
        
        THIS MEANS THAT (MAIN INVARIANT)
        “No cycle was found in the DFS subtree rooted at u.”

        we then go ahead and process(node) (add to list/set)
        """