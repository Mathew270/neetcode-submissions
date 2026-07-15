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
                res.append(0)
                i -= 1
            if i == -1:
                res.append(1)
            else:
                res.append(digits[i] + 1)
                for n in range(i-1, -1, -1):
                    res.append(digits[n])
                return res[::-1]

        return res[::-1]

            