class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        temp = [float("inf")] * n

        dist[src] = 0
        temp[src] = 0

        adj = {i : [] for i in range(n)}

        for u, v, w in flights:
            adj[u].append((w, v))

        # read from dist
        # update in temp
        # after inner loop, dist = temp[:]

        def relax(u, v, w):
            if dist[u] + w < temp[v]:
                temp[v] = dist[u] + w
                q.append((v))

        visit = set()
        q = deque()
        q.append((src))

        res = 0
        while q and res < k + 1:      # 1 stop means we can use 2 edges hence k + 1
            for i in range(len(q)):
                cur = q.popleft()
                for w, nbr in adj[cur]:
                    relax(cur, nbr, w)
            res += 1
            dist = temp[:]

        return dist[dst] if dist[dst] != float("inf") else -1

"""
        for i in range(k + 1):
            for j in range(len(flights)):
                u, v, w = flights[j]
                relax(u, v, w)
            dist = temp[:]
"""    


"""
BELLMAN FORD (USUAL)

E*V

iterate through every edge doesnt matter the order

invariant: after k iterations, 
the shortest paths of length k (k hops away from src) are correctly found so far
--------------------------------------------------------------------------------
BELLMAN FORD (TEMP ARRAY)
E*K

invariant = finds the shortest path from source to dest given that we 
only use k edges

aim is to correctly find the shortest path we can take to a dest from a source
given that we can only use k edges

so we do a level order traversal, but we can only use the estimates we updated
in the previous iteration

any est updates (relax operations) we do in the current iteration cannot be used
to update any other estimate in the curr iteration

(because this means we used more 2 hops to reduce the distance at this iteration)

which defeats our purpose of counting the iterations we can do

to execute this we store our updated estimates of the curr iteration
in a temp array 

and we only look at previous estimates in the dist[]

after the iteration is complete we set dist = temp[:] (copy of temp)

then use update est in the next for loop in temp again and so on...
-----------------------------------------------------------------------------------





"""
