# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curmax = float('-inf')
        res = [0]
        def dfs(node, curmax):
            if not node:
                return
            
            if node.val >= curmax:
                res[0] += 1
                curmax = node.val
            
            dfs(node.right, curmax)
            dfs(node.left, curmax)
        
        dfs(root, curmax)
        return res[0]
