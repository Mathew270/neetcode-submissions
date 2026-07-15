class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    
        if len(hand) % groupSize:
                return False

        count = {}

        for num in hand:
            count[num] = count.get(num, 0) + 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        for i in range(len(hand)//groupSize):
            curMin = 0
            for j in range(groupSize):

                if j == 0:
                    curMin = min_heap[0]
                    count[curMin] -= 1

                    if count[curMin] == 0:
                        heapq.heappop(min_heap)
                else:
                    curNum = curMin + j

                    if curNum not in count or count[curNum] == 0:
                        return False

                    count[curNum] -= 1

                    if count[curNum] == 0:
                        if min_heap[0] != curNum:
                            return False
                        
                        heapq.heappop(min_heap)

                    

        return True
                
                

"""
keep unique values in heap
pop then decrement counter
if counter hits 0, remove from heap

we only use heap values to know the starting number for each group
"""