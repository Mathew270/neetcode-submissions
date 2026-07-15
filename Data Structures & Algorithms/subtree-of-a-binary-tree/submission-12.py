# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            if (not p and q) or (not q and p):
                return False

            if not p and not q:
                return True
            
            return (p.val == q.val) and sameTree(p.right, q.right) and sameTree(p.left, q.left)

        if not subRoot:   # empty tree is always a subtree
            return True

        if not root:      # if root empty when subtree not empty, then false
            return False

        if sameTree(root, subRoot):  # if same tree then done
            return True

        return (self.isSubtree(root.left, subRoot) or   # else check if right or left is same
               self.isSubtree(root.right, subRoot))

