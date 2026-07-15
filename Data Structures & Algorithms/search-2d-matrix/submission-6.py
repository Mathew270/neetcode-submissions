class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list_to_search = 0         # storing index of matrix[], rather than full list
        l, r = 0, len(matrix) - 1  

        while (l < r):
            mid = (r + l) // 2
            if target <= matrix[mid][-1]:
                r = mid
            else:
                l = mid + 1
        
        list_to_search = matrix[l]

        lo, hi = 0, len(list_to_search) - 1

        while (lo < hi):
            mid = (lo + hi) // 2
            if target <= list_to_search[mid]:
                hi = mid
            else:
                lo = mid + 1
        
        return (list_to_search[lo] == target)

"""
we are using binary search where we converge to a single value, rather than
normal one where we checkk arr[mid] == something

for this we need to make sure to set, lo = mid + 1 rather than lo = mid
since lo = mid can cause infinite loop 
(check case when 2 elements remain and ans is the 2nd number)
(lo will always be set to mid, will cause infinite loop)

lo and hi will converge to a single index (we can use either)

1st while loop, 
we obtain which row to search for the target
by elminating rows based on last number in the row and check if its 
greater or equal to target

our while loop is such that it obtains the row with the smallest last number
such that it is bigger or equal to target

2nd while loop,
we do the same but for the actual target 
and we return if the value we converged to is equal to our target
"""
