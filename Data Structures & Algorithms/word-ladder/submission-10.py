class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        adj = defaultdict(list)

        def check_num_diff(s1, s2):
            diff = 0
            for i in range(len(s1)):    # len(s1) == len(s2) constraint
                if s1[i] != s2[i]:
                    diff += 1
            return (diff == 1)

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
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
                if cur == endWord:
                    return res
                for nbr in adj[cur]:
                    if nbr not in visit:
                        q.append(nbr)
                        visit.add(nbr)
            res += 1
        
        return 0


