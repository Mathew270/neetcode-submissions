class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        curr = 0
        res = 0
        i = 0

        diff = [gas[i] - cost[i] for i in range(len(gas))]

        for i in range(len(diff)):
            curr += diff[i]
            if curr < 0:
                curr = 0
                res = i + 1
            
        return res

                    
            


