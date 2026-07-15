class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)  # beginWord not in wordList
        
        adj = defaultdict(list)

        def check_num_diff(s1, s2):   # check if 2 words differ by 1 char
            diff = 0
            for i in range(len(s1)):    # len(s1) == len(s2) constraint
                if s1[i] != s2[i]:
                    diff += 1
            return (diff == 1)

        # create adjList where an edge is between 2 words that differ by 1 char
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
                if check_num_diff(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)   # edges are bidirectional (undirected)

        # use level order bfs for shortest path
        visit = set()
        q = deque()
        q.append(beginWord)
        visit.add(beginWord)

        res = 1   # start at 1 word
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res         # num of words seen in path (including cur)
                for nbr in adj[cur]:
                    if nbr not in visit:
                        q.append(nbr)
                        visit.add(nbr)
            res += 1
        
        return 0
        """
        n = num of words, m = len of each word

        time = O(n^2 * m) for bfs

        max num of edges = n^2 (complete graph)
        bfs = V + E = V + V^2 = V^2

        whenever we pop from bfs we check cur == endWord = O(m)
        hence, O(n^2 * m) for bfs

--------------------------------------------------------------------------------
        time = O(n^2 * m) for creating adj List 
                (could be reduced to m^2*n in another soln)
        
        space = O(n^2) for adj list, (V + E) and E could be n^2
--------------------------------------------------------------------------------
        """

        """
        IMPORTANT (understand when res increments)

        res/ level/ dist in level order bfs, shortest path bfs

        increments after we append all nbrs of all nodes of a level

        eg.

        res = 1     (initialized to 1) (could be 0 for some qns)
        A in q
        append all 3 nbrs of A
        res += 1

        res = 2
        a1,a2,a3 in q
        append all 3 nbr of a1
        append all 3 nbrs of a2
        append all 3 nbrs of a3
        res += 1

        so when u pop from an elem from q thats at level 2
        then u can safely assume that res is also at level 2

        since we havent gone through and appended the lvl 2 elements nbrs yet

        so res wont increment until then (it will stay at level 2) 
        """


