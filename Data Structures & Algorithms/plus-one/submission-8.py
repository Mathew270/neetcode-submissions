class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        i = len(digits) - 1
        added = False

        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits

        while(i >= 0):
            while(digits[i] == 9 and i >= 0):
                #res.append(0)
                digits[i] = 0
                i -= 1
            if i == -1:
                return [1] + digits
            else:
                digits[i] = (digits[i] + 1)
                #for n in range(i-1, -1, -1):
                    #digits[n] = (digits[n])
                #return res[::-1]
                return digits

        #return res[::-1]

"""
handle 2 cases
1) easy case: just add 1 to last digit in list (when its not 9)

2) hard case: last number is 9
create a while loop and run through the array in reverse appending a zero for
every 9 in a row, starting from the last index 

then if we reach the end:
    append a 1 

else:
    add 1 to that element, then copy remaining elements, return reversed list
"""

            