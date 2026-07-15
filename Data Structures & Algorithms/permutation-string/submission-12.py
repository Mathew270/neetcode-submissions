class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashh1 = {}
        hashh2 = {}

        for i in range(len(s1)):
            hashh1[s1[i]] = hashh1.get(s1[i], 0) + 1

        l = 0

        for r in range(len(s2)):
            hashh2[s2[r]] = hashh2.get(s2[r], 0) + 1
            if (r - l + 1) == len(s1):
                if (hashh1 == hashh2):
                    return True
                else:
                    hashh2[s2[l]] -= 1
                    if hashh2[s2[l]] == 0:
                        del hashh2[s2[l]]
                    l += 1
        return False
