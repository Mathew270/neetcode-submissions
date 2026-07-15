class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)         # cannot be set to 0, array could be [-1]
        curMax, curMin = 1,1    # identity number for multiplication

        for n in nums:
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)    # could be n itself, eg. [-2, 5]
            curMin = min(tmp * n, curMin * n, n)

            res = max(res, curMax)
        
        return res

        # why this is a dp problem (despite no usual subprob array)
        # [ 2, 3 , -2, 4]
        #           n

        # when we are at position n (-2) we have computed the curMax and curMin,
        # for the subarray upto the num before that [2, 3]
        # so we are building on top of the previous solutions of subproblems
        # where the base case is the 1st element curmax = curmin = n

        # curMax, curMin = max, min product obtained from any subarray till curr element

        # now why are we finding curMax AND curMin ?
        # this is because we have negative numbers in the array so 
        # we need to know the curMin so when we do curMin * n it will be the new curMax

        # [ 2 , -3, -9]
        #            n
        # curMin = -3, n = -9
        # curMax is set to 27 now   (possible because we kept track of curMin)   

        # possible edge case (when n = 0):
        #  initially we would think that this causes our curMax, curMin to be equal to 0
        # and will always stay that way

        # however, recall that curMax = max(.. , .. , n), since we also check curr element
        # we dont need to worry about it being permanently set to 0

        # things to consider:

        # commented in code itself (res init, curMax/Min init, including n in max(), min())