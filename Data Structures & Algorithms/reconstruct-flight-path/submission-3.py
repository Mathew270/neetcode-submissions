class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)

        for u, v in tickets:
            adj[u].append(v)

        stack = ["JFK"]

        def dfs(node):
            if len(stack) == len(tickets) + 1:
                return True
            
            temp = list(adj[node])
            for i, nbr in enumerate(adj[node]): 
                # iterate over copy (so we dont make changes to list we are iterating over)
                adj[node].pop(i)
                stack.append(nbr)
                if dfs(nbr):          # if path works return True no need to search anym
                    return True

                # if path doesnt work
                stack.pop()
                adj[node].insert(i, nbr)
            
            return False

        dfs("JFK")
        return stack

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

    we cant/not good to iterate over nbrs after 
"""

        