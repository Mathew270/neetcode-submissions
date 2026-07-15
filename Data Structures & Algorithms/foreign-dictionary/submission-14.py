class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c : [] for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            shorter = min(len(w1), len(w2))

            edge_created = False
            for j in range(shorter):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])   # directed edge smaller -> bigger
                    edge_created = True
                    break
            
            if not edge_created and len(w1) > len(w2):
                return ""
        
        res = []
        onPath = set()
        visited = set()
        print(adj)

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

