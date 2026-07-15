class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum < 0:
                    l += 1

                elif threesum > 0:
                    r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                        
        return res














        """
        how this is different from 2sum

        1) we use hashtable, and we can get away with doing 
            for i in range(len(nums)):
                hashh[nums[i]] = i
            because even if a num occurs more than once, its latest index is stored
            so it can only potentially pose an issue if both 1st and 2nd occurence
            of the number are the solution eg. 6 in [3,3]

            but this is actually not an issue since we iterate from the start
            and check if its comp (2nd occurence) is in the hashh and since we store
            latest occurence this isnt a problem

            therefore we can get away with hashing values as keys even if there are
            duplicates

        2) 2 sum = hashtable
           3 sum = sorting + 2 pointers
        """