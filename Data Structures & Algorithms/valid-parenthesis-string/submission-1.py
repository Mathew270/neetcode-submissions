class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxLeft = 0, 0

        for c in s:

            if c == "(":
                minLeft += 1 
                maxLeft += 1

            elif c == ")":
                minLeft -= 1 
                maxLeft -= 1
            
            else:
                maxLeft = maxLeft + 1
                minLeft = minLeft - 1

            if minLeft < 0:
                minLeft = 0

            if maxLeft < 0:
                return False

        return minLeft == 0


"""
go through each char in string

if (
    increment max, min by 1

if )
    decrement max, min by 1

if *
    max = increment
    min = max(0, decrement)

if max < 0:
    return false
"""