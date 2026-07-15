class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}

        def back(i, j):

            if (i,j) in dp:
                return dp[(i,j)]

            if i + j == len(s3):
                return True

            if i == len(s1):
                return s2[j:] == s3[i + j:]

            if j == len(s2):
                return s1[i:] == s3[i + j:]

            c1, c2, c3 = s1[i], s2[j], s3[i + j]

            if c1 != c3 and c2 != c3:
                return False
            
            if c1 == c3 and c2 == c3:
                dp[(i,j)] = back(i + 1, j) or back(i, j + 1)
            
            elif c1 == c3:
                dp[(i,j)] = back(i + 1, j)
            
            elif c2 == c3:
                dp[(i,j)] = back(i, j + 1)
            
            return dp[(i,j)]

        return back(0,0)
            

