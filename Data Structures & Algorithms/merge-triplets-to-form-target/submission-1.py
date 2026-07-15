class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            
            else:
                if x == target[0]:
                    first = True
                
                if y == target[1]:
                    second = True

                if z == target[2]:
                    third = True

        return first and second and third

"""
actually very easy question

1)
1st disregard any triplet if they have any number greater than the number we need
at each position  (impossible to incorporate them since we using max())

2)
then we just need to see if each number in our triplet 
exists in any of the remaining triplets

(because of 1) we know all other triplets will have no.s less than our one,
which is filtered out by max())
"""