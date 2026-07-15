class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for w in strs:
            res.append(str(len(w)))
            res.append("#")
            res.append(w)                       #O(N)
        return "".join(res)
        """
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w      #O(n^2)
        return res
        """

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            length = int(s[i:j])   # j is at # so not included
            i = j + 1              # set to start of word (after #)
            j = i + length         # set to after word ends
            res.append(s[i:j])     # append word to res
            i = j

        return res
