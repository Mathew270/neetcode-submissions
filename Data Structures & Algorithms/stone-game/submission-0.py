class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {}

        def dfs(player, i, j):
            if (player, i, j) in dp:
                return dp[(player, i, j)]

            if i > j:
                return 0
            
            if i == j:
                return piles[i]

            if player == 'B':
                dp[(player, i, j)] = min(piles[i] + dfs('A', i + 1, j), piles[j] + dfs('A', i, j - 1))
                return dp[(player, i, j)]

            if player == 'A':
                dp[(player, i, j)] = max(piles[i] + dfs('B', i + 1, j), piles[j] + dfs('B', i, j - 1))
                return dp[(player, i, j)]

        alice = dfs('A', 0, len(piles) - 1)

        return alice > sum(piles) // 2

        
        