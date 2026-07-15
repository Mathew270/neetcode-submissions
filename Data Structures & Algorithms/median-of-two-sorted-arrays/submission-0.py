class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listt = sorted(nums1 + nums2)
        if len(listt) % 2:  #odd
            return listt[len(listt) // 2]
        else:
            return ( listt[len(listt)//2 - 1] + listt[len(listt)//2] )/ 2