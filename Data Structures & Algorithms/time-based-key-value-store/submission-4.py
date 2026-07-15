# All the timestamps timestamp of set are strictly increasing.
# so we know values are sorted according to timpestamps, enabling binary search
# (given in constraints)

class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        l , r = 0, len(values) - 1

        while(l <= r):       # trying to obtain max number less than timestamp
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:  
                res = values[mid][0]
                l = mid + 1
        # if value too less then we still need to store it as a possible soln
        # but we cant just reduce search space to include mid (low = mid)
        # because this can cause infinite loop (when 2 elements 
        # remain and we always set    low = mid)
        # so we update a created res variable whenever we are at this case
        # then set l = mid + 1 (recorded current mid at res)

            else:
                r = mid - 1
        # larger than timestamp so can never be a soln

        return res