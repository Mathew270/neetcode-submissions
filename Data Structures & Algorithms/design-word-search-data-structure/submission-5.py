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

        def dfs(j, root):

            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":  # search every child
                    for child in curr.children:
                        if dfs(i + 1, curr.children[child]):
                            return True
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.isEnd
        
        return dfs(0, self.root)


