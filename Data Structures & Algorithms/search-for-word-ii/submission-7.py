class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
    
        def dfs(x, y, word, node):
            if x >= rows or y >= cols or x < 0 or y < 0 or (x,y) in visit or board[x][y] not in node.children:
                return
            
            node = node.children[board[x][y]]
            word += board[x][y]
            visit.add((x,y))
            if node.isEnd:
                res.add(word)

            dfs(x + 1, y, word, node)
            dfs(x, y + 1, word, node)
            dfs(x - 1, y, word, node)
            dfs(x, y - 1, word, node)
            
            visit.remove((x,y))

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,"",root)
        
        return list(res)

"""
less efficient way:
    do word search 1 for all words in the list
    w * n*m * 3^L

    w = no. of words
    n*m = size of board
    L = length of longest word / avg length of words

    we do dfs() starting at every cell and check if word is there
    repeat this process for all words

optimized (Trie + dfs()):

    we can remove the W factor
    as in we do not need to repeat the process for all words

    idea:
        to run dfs() starting from every cell once
        and check along the way if the prefix is in the words list
        we use a trie for this

        eg. start dfs at 
        b -> a -> c        (in Trie but not end of word)   (continue dfs)
                    -> c   X (not in trie)  (dont continue this dfs)
                    -> k   (in Trie) (append to res)
"""