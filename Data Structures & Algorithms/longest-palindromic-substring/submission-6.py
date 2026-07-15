class Solution:
    def longestPalindrome(self, s: str) -> str:
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