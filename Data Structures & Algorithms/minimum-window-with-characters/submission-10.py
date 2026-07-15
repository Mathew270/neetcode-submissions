class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashh1 = {}
        hashh2 = {}

        for i in range(len(t)):
            hashh1[t[i]] = hashh1.get(t[i], 0) + 1
        
        l = 0
        res_len = float('inf')
        resL = 3
        resR = 2

        def check():
            for i in hashh1:
                if i not in hashh2:
                    return False
                if hashh2[i] < hashh1[i]:
                    return False
            return True

        for r in range(len(s)):
            if s[r] in hashh1:
                hashh2[s[r]] = hashh2.get(s[r], 0) + 1

            while(check()):
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    resL, resR = l, r
                if s[l] in hashh2:
                    hashh2[s[l]] -= 1
                    #if hashh2[s[l]] == 0:
                        #del hashh2[s[l]]
                l += 1

        return s[resL : resR + 1]