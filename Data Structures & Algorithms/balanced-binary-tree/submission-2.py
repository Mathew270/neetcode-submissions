# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            hleft, hright = dfs(root.left), dfs(root.right)
            
            if abs(hleft[1] - hright[1]) <= 1 and hleft[0] and hright[0]:
                return [True, 1 + max(hleft[1], hright[1])]
            
            return [False, 0]

        return dfs(root)[0]
