# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return False
        if (not root and subRoot) or (not subRoot and root):
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        else:
            return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)