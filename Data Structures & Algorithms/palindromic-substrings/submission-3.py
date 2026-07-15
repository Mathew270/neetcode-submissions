class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        total = 0
        res = []

        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                total += 1
                res.append(s[l:r+1])
                l -= 1
                r += 1
                
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                total += 1
                res.append(s[l:r+1])
                l -= 1
                r += 1
        
        print(res)
        return total
