class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c : set() for w in words for c in w }  # include all chars in all words

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            shorter = min(len(w1), len(w2))

            edge_created = False
            for j in range(shorter):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])   # directed edge smaller -> bigger
                    edge_created = True
                    break
            
            if not edge_created and len(w1) > len(w2): 
                # if one owrd contained in another and if before word is longer than next one
                return ""
        
        res = []
        onPath = set()
        visited = set()

        def dfs(node):
            if node in onPath:
                return False       # cycle found
            elif node in visited:
                return True
            onPath.add(node)

            for nbr in adj[node]:
                if not dfs(nbr):
                    return False  # cycle found

            onPath.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])

"""
only hard part about problem was creating adjacency list 
where edge is created by comparing 2 adjacent elements

wrong initial thinking:
compare group wise 
(compare all letters starting chars then, all letters starting with H, ...)
(no need to this since we can compare just pairwise and make edges there)

after this its just topological sort
using post order dfs cycle detection or
kahns topo sort using bfs
"""

"""
can start post order dfs from any node not just source
because when u do dfs(node) it will add to stack 
[last, 2nd last...node] everything that comes after node to node

now when u do dfs(node_prereq)
it will add to stack only after node 
which still maintains our reverse order

[last, 2nd last...node.....node_prereq (with their own dependencies)]

in fact u have to do 
        for c in adj:
            if not dfs(c):
                return ""
so we even include disconnected components
"""

"""
however khans topo sort using bfs
u can only start from source

because the very definition of the algo is to only append to q those 
nodes that have indegrees of 0

so at first only the source has indegrees 0

since we append all the sources to q, we are sure to include all 
connected components

and wont have to do 
        for c in adj:
            if not bfs(c):
                return ""
"""

