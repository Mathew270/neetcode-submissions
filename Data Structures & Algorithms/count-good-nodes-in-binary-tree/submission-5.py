# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_seen = float("-inf")
        res = [0]

        def dfs(root, max_seen):
            if not root:
                return
            
            if root.val >= max_seen:
                res[0] += 1
                max_seen = max(max_seen, root.val)

            dfs(root.left, max_seen)
            dfs(root.right, max_seen)

        dfs(root, root.val)
        return res[0]

