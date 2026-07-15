class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # use union find 
        # start of with n connected components
        # call find for each edge
        # if different components union
        # else return edge

        n = len(edges)
        rank = [1] * n    
        par = [i for i in range(n)]

        def find(x):
            root = x
            while par[root] != root:
                root = par[root]
            
            while par[x] != x:    # path compression
                tmp = par[x]
                par[x] = root
                x = tmp
            
            return root
        
        def union(x,y):
            root1 = find(x)
            root2 = find(y)

            if root1 == root2:
                return
            
            #bigger should be parent of smaller

            if rank[root1] < rank[root2]:
                par[root1] = root2
                rank[root2] += rank[root1]
            
            else:
                par[root2] = root1
                rank[root1] += rank[root2]

        for v1, v2 in edges:
            if find(v1-1) != find(v2-1): # since vertices are 1 indexed we do -1
                union(v1-1, v2-1)
            else:
                return [v1,v2]