# All the timestamps timestamp of set are strictly increasing.
# so we know values are sorted according to timpestamps, enabling binary search
# (given in constraints)

class TimeMap:

    def __init__(self):
        self.keystore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.keystore or self.keystore[key] == []:
            return res
        listt = self.keystore[key]
        l, r = 0, len(listt) - 1

        while l <= r:
            mid = (l + r) // 2

            if listt[mid][1] > timestamp:
                r = mid - 1
            else:
                res = listt[mid][0]
                l = mid + 1
        
        return res


        # if value too less then we still need to store it as a possible soln
        # but we cant just reduce search space to include mid (low = mid)
        # because this can cause infinite loop (when 2 elements 
        # remain and we always set    low = mid)
        # so we update a created res variable whenever we are at this case
        # then set l = mid + 1 (recorded current mid at res)

        
        # larger than timestamp so can never be a soln