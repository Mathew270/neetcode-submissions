# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]
        dp = {}

        def dfs(root):
            if root in dp:
                return dp[root]

            if not root:
                return 0
            
            dp[root.left] = dfs(root.left)
            dp[root.right] = dfs(root.right)

            left, right = dp[root.left], dp[root.right]

            dp[root] = max(root.val, 
                        root.val + left, 
                            root.val + right)

            max_sum[0] = max(max_sum[0], dp[root], (root.val + left + right))
            return dp[root]

        dfs(root)
        return max_sum[0]

        
        

            