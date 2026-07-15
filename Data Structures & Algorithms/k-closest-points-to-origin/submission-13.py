import heapq
import math
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_to_pts = defaultdict(list)    #dist -> list(of points)  

        for x,y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)  #dist from origin
            dist_to_pts[dist].append([x,y])
        

        heap = list(dist_to_pts.keys())
        heapq.heapify(heap)

        res = []

        while(len(res) < k):
            dist = heapq.heappop(heap)
            curr_pts = dist_to_pts[dist]
            for p in curr_pts:
                res.append(p)
                if len(res) == k:
                    return res


"""
        for d in dist_to_pts:
            if len(heap) < k:
                heapq.heappush(heap, d)
            else:
                heapq.heappushpop(heap, d)
        
        res = []
        for d in heap:
            res += dist_to_pts[d]
        
        return res
"""