class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    
        if len(hand) % groupSize:
                return False

        count = {}

        for num in hand:
            count[num] = count.get(num, 0) + 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        for i in range(len(hand)//groupSize):  # for each group
            curMin = 0
            for j in range(groupSize):    # for each element in group
                
                if j == 0:                # if 1st element in group (get the current minimum from heap)
                    curMin = min_heap[0]
                    count[curMin] -= 1

                    if count[curMin] == 0:        # remove from heap if count is 0, all instances of that element is used
                        heapq.heappop(min_heap)
                
                else:                     # for other nums
                    curNum = curMin + j   # if 2 is our minimum, we need 3, 4, 5 next to complete a group of size 4

                    if curNum not in count or count[curNum] == 0:  
                        return False     # if those nums dont exist, can return false (cannot make group)

                    count[curNum] -= 1

                    if count[curNum] == 0:          
                        if min_heap[0] != curNum:
                            return False
                        
                        heapq.heappop(min_heap)

                    # if count of an element becomes 0, we need to remove it
                    # but what if element is not minimum in heap ?
                    # IT HAS TO BE
                    # if its not the minimum element, then its impossible to create another group

                    # eg. we have 3,4,5  but count[4] is now 0
                    # this means we can never use the remaining 3, 5 to create a valid group without 4
                    # thats why we can only continue with the question if its the minimum num's count that became 0

        return True
                
                

"""
keep unique values in heap
pop then decrement counter
if counter hits 0, remove from heap

we only use heap values to know the starting number for each group
then check if remaining numbers in grp are in count{}
"""