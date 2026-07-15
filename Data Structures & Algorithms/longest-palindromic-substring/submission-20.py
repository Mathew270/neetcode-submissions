class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        b,e = 0,0
        maxL = 0

        for i in range(n):
            l, r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxL:
                    maxL = r - l + 1
                    b,e = l, r
                l -= 1
                r += 1
            
            l,r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxL:
                    maxL = r - 1 + 1
                    b, e = l, r
                l -= 1
                r += 1

        return s[b:e + 1]

        """
        n = len(s)
        dp = {}
        maxL = 0
        l,r = 0,0

        def is_palindrome(i,j):
            if i > j:
                return True

            if (i,j) in dp:
                return dp[(i,j)]

            elif i == j:
                dp[(i,j)] = True
                
            elif s[i] == s[j]:
                dp[(i,j)] = is_palindrome(i+1, j-1)    

            else:
                dp[(i,j)] = False
            
            return dp[(i,j)]

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j) and j - i + 1 > maxL:
                    maxL = j - i + 1
                    l,r = i, j

        return s[l:r+1]
        """           






        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0

        for i in range(n):
            dp[i][i] = True

        for length in range(2,n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if length > max_len:
                            max_len = length
                            start = i
                #else:
                #    dp[i][j] = False

        return s[start:start + max_len]
        """