class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles
        # n - 1 edges

        # given edges: we can check if len(edges) == n - 1
        # if above is true still need to check if its connected

        if len(edges) != n - 1:  # no. of edges != n - 1
            return False

        visited = set()

        def dfs(n):          # add node to visited 
            if n in visited:
                return
            visited.add(n)

            for nbr in adj[n]:
                dfs(nbr)

        # create adj_list
        adj = {i : [] for i in range(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)  # constraint tells us no duplicate edges

        
        dfs(0)     
        return len(visited) == n  # check if all nodes are connected

"""
time = O(V) to create adj list

(we only create adj_list if e = v - 1)
so O(V + V) = O(V)
----------------------------------------------------------

OPTIMIZATION 
if we were given adj list:

then also O(v)
------------------------------------------------------------
because

we iterate through all edges 
since edges are undirected we will have 2 * actual no. of edges

if the number of edges we see reaches 2n - 1. we know its not a tree

2n - 1 because
a tree can only have n-1 edges

but we dont check for n-1 here
rather 2*(n-1)  since adj_list has twice the number of actual edges

2*(n-1) still a valid tree

invalid when 2*(n-1) + 1 = 2n - 2 + 1 = (2n - 1)


however once we see it equals the right amount of edges we still need to see
if graph is connected. we do dfs()

but its O(v) here since num. edges = 2n-1 (n==v) (so O(V))
"""