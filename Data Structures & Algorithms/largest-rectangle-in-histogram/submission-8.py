class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_arr = 0

        for i,h in enumerate(heights):
            last_popped_idx = i
            while(stack and h < stack[-1][1]):
                pop_i, pop_h = stack.pop()
                last_popped_idx = pop_i
                arr = (i - pop_i) * pop_h
                max_arr = max(max_arr, arr)
            stack.append((last_popped_idx, h))

        for i, h in stack: # elements that can be extended till end of array
            arr = (len(heights) - i) * h
            max_arr = max(max_arr, arr)
        
        return max_arr

        """
        (this qn) find position of 1st height smaller than current one
    (dailt temps) find position of 1st temp greater than current one
use the difference in indeces (popped element(s) and incoming element)
to calculate width (this qn) / gap (daily temp) (same thing)

-----------------------------------------------------------------------------------
        height can extend backwards 
        (this is handled by modifying the start index to calculate area)
        (the start index for the incoming element by default is the actual index,
        but if incoming element causes the popping of elements then the 
        start_index for the incoming element is set to the index of the last_popped_index

        since it can extend backward till the index of last_popped_idx

        initial mistake corrected after tracing: setting start index to no. of elems popped
        this caused incorrect answer since no. of elems popped does not equal start_idx
        of last popped element, since that last popped element could have popped elements
        also making its index decrease from before

        thereby causing no. of pops (difference in idx of incoming element and actual index
        of last popped elemnt) NOT EQUAL to start_idx of last popped element

        test case (28 neetcode)

-----------------------------------------------------------------------------------
        u update the results for those elements u are popping out of stack
        which happens when the incoming element is smaller than the top

        but for the elements that remain in stacked (never popped)

        u have to calculate their areas and update max if needed (what last for loop does)

        these elements extend till the end of the arr 
        (need intuition to realise that, not so trivial) 
        so arr = (len - start_idx)  * height
        
        """