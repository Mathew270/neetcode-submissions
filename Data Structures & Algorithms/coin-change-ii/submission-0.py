class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def back(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]

            if amt == 0:
                return 1
            
            if amt < 0 or i >= len(coins):
                return 0
            
            dp[(i, amt)] = back(i, amt - coins[i]) + back(i + 1, amt)
            return dp[(i, amt)]

        return back(0, amount)