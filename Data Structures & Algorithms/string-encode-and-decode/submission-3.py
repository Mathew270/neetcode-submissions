class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            length = int(s[i:j])   # j is at # so not included
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
