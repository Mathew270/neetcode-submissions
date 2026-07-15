class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
           # no need another trie class just have this method take self as argument (trieNode as arg)
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create Trie
        root = TrieNode()
        rows, cols = len(board), len(board[0])

        for word in words:
            root.addWord(word)

        res = set()
        word = ""
        visited = set()

        def dfs(node, x, y, word):
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] not in node.children or (x,y) in visited:
                return

            visited.add((x,y))
            word += board[x][y]
            node = node.children[board[x][y]]
            if node.isEnd:
                res.add(word)
            
            dfs(node, x + 1, y, word)
            dfs(node, x - 1, y, word)
            dfs(node, x, y + 1, word)
            dfs(node, x, y - 1, word)

            visited.remove((x,y))

        for i in range(rows):
            for j in range(cols):
                dfs(root, i, j, word)

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
                    

    in our Trie class we dont need a search()
    we just check in our dfs() if the current node we are at is the end of a word or not

    and we return from dfs() if (current letter) (board[x][y])
    is not in node.children  
"""