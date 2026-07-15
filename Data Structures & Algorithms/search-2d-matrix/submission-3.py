class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list_to_search = 0 # storing index
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
