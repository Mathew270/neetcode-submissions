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