class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow  

        """
        floyds tortoise and hare algorithm (lowkey cant solve without seeing before)
        cycle detection algorithm in linked list
        this uses O(1) space and O(n) time 
        
        (can easily solve wo above algo if we use O(n space))

        1) set a fast and slow pointer
        2) slow moves 1 step, fast moves 2 steps
        3) find the node where fast and slow meet

        4) set a new slow pointer
        5) old slow and new slow move 1 step
        6) find where they both meet 

        7) that meeting point is the answer (duplicate number)
        """
        # IMP
        
        # the index tells us the duplicate number not the element at index
        # because if element at index has multiple pointers to it
        # the num that corressponds to the multiple pointers is the duplicate 
        # hence we return slow and not nums[slow]
                