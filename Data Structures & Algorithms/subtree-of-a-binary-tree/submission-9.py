# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]
        
        def sameTree(p, q):
            if (not p and q) or (not q and p):
                return False

            if not p and not q:
                return True
            
            return (p.val == q.val) and sameTree(p.right, q.right) and sameTree(p.left, q.left)

        def dfs(root):
            if not root:
                return
            
            res[0] = res[0] or sameTree(root, subRoot)

            if not res[0]:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return res[0]

