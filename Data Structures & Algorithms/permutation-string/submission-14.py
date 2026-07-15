class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashh1 = {}
        hashh2 = {}

        for i in range(len(s1)):   # create count table for s1
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

"""
things learnt

1) 1st add s2[r] to whatevr data structure ur using then only do the (r-l+1)
    check. because if u do r-l+1 check before adding s2[r] 
    (initial iteration)
    u wrongly indicate
    that u have r-l+1 (0-0 + 1) 1 element in ur hash table when u actually 
    no elements

2) remember to del the entry in the hashtable when count[entry] = 0.
    since our check is hash1 == hash2. we need to make sure those with count 0
    are removed so that the == check wont be affected.

    hashh1 wont equal hashh2 if hash1 has no entry "L" but hashh2 has an entry
    "L" of count 0. when actually we want this scenario to be equal 
"""