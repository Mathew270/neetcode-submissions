class Solution:
    def trap(self, height: List[int]) -> int:

        pref = [0] * len(height)
        post = [0] * len(height)

        pref[0], post[-1] = height[0], height[-1]

        res = 0

        for i in range(1, len(height)):
            pref[i] = max(pref[i-1], height[i])
        
        for i in range(len(height)-2, 0, -1):
            post[i] = max(post[i+1], height[i])

        print(pref)
        print(post)

        for i in range(1, len(height)-1):
            water = min(pref[i-1], post[i+1]) - height[i]
            if water > 0:
                res += water
        
        return res

        