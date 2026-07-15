class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        sett = set()
        sett.add(beginWord)

        if beginWord == endWord:
            return 1

        for w in wordList:
            sett.add(w)
        
        if endWord not in sett:
            return 0
        
        adj = defaultdict(list)

        def check_num_diff(s1, s2):
            diff = 0
            for i in range(len(s1)):    # len(s1) == len(s2) constraint
                if s1[i] != s2[i]:
                    diff += 1
            return (diff == 1)

        w_list = list(sett)

        for i in range(len(w_list)):
            for j in range(i+1, len(w_list)):
                w1, w2 = w_list[i], w_list[j]
                if check_num_diff(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)

        visit = set()
        q = deque()
        q.append(beginWord)
        visit.add(beginWord)

        res = 1   # start at 1 word
        while q:
            for i in range(len(q)):
                cur = q.popleft()

                for nbr in adj[cur]:
                    if nbr not in visit:
                        if nbr == endWord:
                            return res + 1

                        q.append(nbr)
                        visit.add(nbr)
            res += 1
        
        return 0


