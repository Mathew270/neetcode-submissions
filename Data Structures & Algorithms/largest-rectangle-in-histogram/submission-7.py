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