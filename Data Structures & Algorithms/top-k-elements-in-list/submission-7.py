import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []

        for num in count:
            if len(heap) < k:
                heapq.heappush(heap, (count[num], num))
            
            else:
                heapq.heappushpop(heap, (count[num], num))

        res = []
        
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res[::-1]

        # BUCKET SORT
        # solution explanation:  O(N)
        # first we find the count hashmap (count of each num)

        # we create a frequency list, where each element is a list of nums of that count
        # at that index
        # the fact that each index represents the count we only need the list to be of
        # length (len(nums) + 1).  (0 to len(nums)) 
        # (as those are the only possible no. of times a number can appear in the list)

        # after making this list of list called list

        # we iterate throught count{} and append every num with a 
        # particular count to the list at that count index in freq

        # after doing this for all nums,
        # we iterate through freq in reverse order (largest to smallest count)

        # and store the numbers in the res[] array. till len(res) == k

        # we are guaranteed that there is a unique solution, so we dont need to 
        # add the numbers 1 by 1 from freq[i] list to res, but rather can just add
        # enitre list (freq[i]) to res

        # ALTERNATIVE SOLUTIONS

        # using max-heap
        # create count{}
        # heapify based on count O(N)
        # extract Max k times O(k log N)

        # using min-heap
        # create count{}
        # aim is to have the heap only store k elements (count)

        # insert each elem
        # if size > k:
        #   extract Min
        # O(N log k)

        # Using normal sorting O(N log N)
        # sort count.values(), retrieve k highest counts

        # the trick is to know that we dont need to sort counts rather append each elem
        # to the list of that specific count (freq[])