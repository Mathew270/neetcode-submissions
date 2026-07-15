class Solution:
    def maxDifference(self, s: str) -> int:
        dict1 = {}
        mineven = float("inf")
        minodd = float("inf")
        maxeven = float("-inf")
        maxodd = float("-inf")

        for c in s:
            dict1[c] = dict1.get(c, 0) + 1

        for num in list(dict1.values()):
            if num % 2:
                maxodd = max(maxodd, num)
                minodd = min(minodd, num)

            else:
                maxeven = max(maxeven, num)
                mineven = min(mineven, num)

        return (maxodd - mineven)
        