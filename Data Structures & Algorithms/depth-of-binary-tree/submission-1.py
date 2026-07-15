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
            
            return 1 + max(dfs(root.left), dfs(root.right))

        return dfs(root)

"""
leaf is of depth 1

so if null then return 0 (base case)

recurse = 1 + max(r, l)
"""