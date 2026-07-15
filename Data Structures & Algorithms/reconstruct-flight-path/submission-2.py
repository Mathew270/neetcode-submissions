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
                if dfs(nbr):          # if path works return
                    return True

                # if path doesnt work
                stack.pop()
                adj[node].insert(i, nbr)
            
            return False

        dfs("JFK")
        return stack
                

        