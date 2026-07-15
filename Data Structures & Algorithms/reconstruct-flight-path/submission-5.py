class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False
            
        dfs("JFK")
        return res

"""
Good qn many points of learning

1) how to get it in lexicographical order ?

    rlly naive way is to find all valid paths then sort 
    but we rlly dont need to do this

    we can sort the adj list, then everytime we iterate over nbrs of a node
    we will be doing it in lexico order, so the 1st valid path 
    we find is the right one


2) in this qn unlike usual dfs() qns we can visit nodes again
    even along the current path (not just in diff paths)
    however we are not allowed to revisit edges along current path
    (cant use 1 ticket multiple times)

    the way we handle not visiting nodes again is using a visit set()
    here we cant do this since we can visit nodes again (even in current path)

    the way we handle not revisiting edges is by removing the edge
    from the adjecency list

    adj[node].pop(i)

3) problems to resolve when doing the above

    1 )we cant/not good to iterate over nbrs when modifying the nbr list

        so to do this we create a copy temp and iterate over that
    
    2) how do undo our pop (during backtrack)
        since we need to find a valid path, backtracking is involved and we 
        need to undo our changes 
        (adding the edge back, so we can use it in our next path we r checking)
        (pop city (nbr) from stack)

        if we naively append back to adj[node] we need to sort it again

        to avoid this we note the index we removed from then do .insert(i, nbr)
        .insert is O(n) but its better than sorting again
        to get the index we can easily call enumerate on nbr list

        ##
        for i, nbr in enumerate(adj[node]): 
                # iterate over copy (so we dont make changes to list we are iterating over)
                adj[node].pop(i)
                stack.append(nbr)
                if dfs(nbr):          # if path works return True no need to search anym
                    return True

                # if path doesnt work
                stack.pop()
                adj[node].insert(i, nbr)
        ##
    
4)  subtle but worth noting (similar idea used in multiple qns)

        if dfs(nbr):    
            return True
    
        we are done as soon as we find the 1st valid path 
        (since we sorted lexi, our 1st valid path is our ans)

        so we do an if check like this while calling dfs for all nbrs
        if True, this result just propagates back to all other calls
        and we are done

        SIMILAR IDEA IN COURSE SCHEDULE (CYCLE DETECTION)

            if not dfs(node):
                return False

        for this qn we return as soon as dfs() returns False 
        (node in onPath) (when we detected a cycle)

        so our base case should have the condition where we are finally done (obvious)

5)  MINOR THINGS TO NOTE:

    1)  if len(stack) == len(tickets) + 1:  (base case for recursion)
                return True

        num of cities == tickets + 1 (no ticket to city we are starting from)

    2)  stack = ["JFK"]
        we do this because during our recursion dfs()
        we never will never actually append the inital JFK because
        we pass in "JFK" and iterate through nbrs adding them to stack
        based on path taken 
        (removing them later if path is invalid) via backtracking

        the reason we didnt hv to do this for other qns
        is because we maintain a visit() set for nodes
        and when we call dfs(node) the node gets added to visit()

        we arent doing that for this qn tho 
        (since nodes can be visited again)
        (constraint is on edges) (handled by removing endNode from adjList)

    3)  not related to this qn but:
        when initializing adjList 
        have in the back of ur mind whether ur adding all possible nodes
        or just nodes in the edge list (some nodes could be excluded)

        this point is more relevant for course schedule

        when we check if (finished == numCourses)

        for this qn its fine since our nodes are only from edge list

"""

        