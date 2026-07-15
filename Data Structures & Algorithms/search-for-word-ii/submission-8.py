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

        # add all words to Trie
        for w in words:
            root.addWord(w)

        res = set()      # incase there are duplicate words we only return unique ones
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(x,y, word, node):
            # if (out of bounds) or (letter not in Trie) or (alr visited) then return nothing
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] not in node.children or (x,y) in visit:
                return

            visit.add((x,y))

            cur = node.children[board[x][y]]
            word += board[x][y]
            if cur.isEnd:
                res.add(word)

            dfs(x + 1, y, word, cur)
            dfs(x - 1, y, word, cur)
            dfs(x, y + 1, word, cur)
            dfs(x, y - 1, word, cur)

            visit.remove((x,y))  # clear visited for next dfs() starting from next cell

        for i in range(rows):
            for j in range(cols):
                dfs(i,j, "", root)  # start dfs from every cell with empty string and root of Trie
        
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