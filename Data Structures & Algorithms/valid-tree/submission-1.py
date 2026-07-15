class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles
        # n - 1 edges

        # given edges: we can check if len(edges) == n - 1
        # if above is true still need to check if its connected
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

        if len(edges) != n - 1:  # no. of edges != n - 1
            return False
        
        dfs(0)     
        return len(visited) == n  # check if all nodes are connected