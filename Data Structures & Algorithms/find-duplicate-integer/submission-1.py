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
        
        # the index tells us the duplicate number not the element at index
        # because if element at index has multiple pointers to it
        # the num that corressponds to the multiple pointers is the duplicate 
                