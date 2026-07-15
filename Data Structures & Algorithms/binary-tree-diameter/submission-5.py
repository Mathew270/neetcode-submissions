# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]

        def dfs(root):
            if not root:
                return 0

            heightleft = dfs(root.left)
            heightright = dfs(root.right)

            maxx[0] = max(maxx[0], heightleft + heightright)
            return 1 + max(heightleft, heightright)

        dfs(root)
        return maxx[0]