class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxLeft = 0, 0   #minLeft = min number of opening paranthesis
                                  #maxleft = max number of opening paranthesis

        # if maxLeft is ever negative eg. " (( ))) " then we return false

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
for this question you only actually need to keep track of minLeft mainly
the only reason we track maxLeft, is to return false if it ever reaches negative
(maxLeft is negative when => more closing than opening paranthesis at any given point)
impossible to recover from such a situation hence we return false immediately

minLeft is used to track the min number of paranthesis such that it is still valid
if it goes to negative we reset it to 0

go through each char in string

if (
    increment max, min by 1

if )
    decrement max, min by 1

if *
    max = increment
    min = decrement

if min < 0:
    min = 0   (reset min to 0)

if max < 0:
    return false
"""