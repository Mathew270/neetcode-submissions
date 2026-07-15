class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []

        for idx, h in enumerate(heights):
            last_popped_idx = idx

            while stack and h < stack[-1][1]:
                top_idx, top_h = stack.pop()
                area = (idx - top_idx) * top_h
                max_area = max(max_area, area)

                last_popped_idx = top_idx

            stack.append((last_popped_idx, h))

        for idx, h in stack:
            area = (len(heights) - idx) * h
            max_area = max(max_area, area)

        return max_area