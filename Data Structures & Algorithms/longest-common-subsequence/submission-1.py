class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

"""
base cases:

    "" c r a b t

""  0  0 0 0 0 0
c   0
a   0
t   0

length of longest substring when either string is "" is 0

"" in crabt = "" in common (length = 0)

cat in "" = "" in common (length = 0)

each subproblem:
    legnth of longest subsequence between index 0 to i for w1 and 0 to j for w2

relation:
    if w1[i] == w2[j]:
        then dp[i][j] = 1 + dp[i-1][j-1]

    eg.
        ca(t) and crab(t) the length of longest subsequence here is
        since we know theyre last letter are equal we can add 1 to
        length of longest subsequence of w1, w2 till before that letter

    if w1[i] != w2[j]:

        then dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        since the last letters arent equal we can either check
        length of longest subs of w1, w2 (excluding last)   dp[i][j-1]
        or
        length of longest subs of w2, w1 (excluding last)   dp[i-1][j]

        and take max of that

why this works:

    swea t ing
    shet n i

    since n and t are different  we have 2 choices

    either take lcs of sweat, shet  or swea, shetn

    the former is longer with lcs = set

    --------
"""










