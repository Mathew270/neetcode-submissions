class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def back(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                dp[(i, j)] = back(i + 1, j + 1)

            else:
                dp[(i, j)] = 1 + min(back(i + 1, j), back(i, j + 1), back(i + 1, j + 1))

            return dp[(i, j)]

        return back(0,0)

"""
solved with hints so isnt too hard

if we reach end of a word   (base case)

If index i goes out of bounds, 
we return the number of remaining characters in word2 (using insert operations). 
If index j goes out of bounds, 
we return the number of remaining characters in word1 (using delete operations).


if 2 letters are equal then we dont do any operation and move on to next letters

if word1[i] == word2[j]:
    dp[(i, j)] = back(i + 1, j + 1)


Otherwise, we have three choices: 

insert the character at the current index of word1 (increment j), 
delete the current character of word1 (increment i), 
or replace the character at index i in word1 (increment both i and j).

else:
    dp[(i, j)] = 1 + min(back(i + 1, j), back(i, j + 1), back(i + 1, j + 1))


since all we need is the min number of operations used, we can cache results
(repeated subproblems)

"""

            