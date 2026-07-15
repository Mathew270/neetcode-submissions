# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            heightright = 1 + dfs(root.right)
            heightleft = 1 + dfs(root.left)

            return max(heightright, heightleft)

        return dfs(root)