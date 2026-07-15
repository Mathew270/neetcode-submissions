class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(j, node):

            if j == len(word):
                return node.isEnd
            
            char = word[j]

            if char == ".":
                for child in node.children:
                    if dfs(j + 1, node.children[child]):
                        return True
                return False
            
            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(j + 1, node.children[char])
        
        return dfs(0, self.root)

"""
search is similar to normal trie search except when its "."
we go through all children and repeat the same process

when a word ends with .
the for loop doesnt execute since in range(len, len)
so we check return curr.isEnd (meaning we return if that child is the end)

so we satisfy the condition of getting ans as same no. of letters as word in this case
"""
