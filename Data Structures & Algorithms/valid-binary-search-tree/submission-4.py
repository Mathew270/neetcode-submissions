# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(low, root, high):
            if not root:
                return True
            
            if root.val >= high or root.val <= low:
                return False
            
            return valid(low, root.left, root.val) and valid(root.val, root.right, high)

        return valid(float("-inf"), root, float("inf"))
        
"""
Actually not really so simple at first
dfs with root + 2 variables

The idea here is to evaluate each node while traversing from the top,
we check if each node.val obeys the the range it must be in

the range is decided based on the lowest and highest value a node can have

for the left subtree, 
    can go as low as "low"
    cannot be higher than "root.val"

for the right subtree, 
    can go as high as "high"
    cannot be lower than "root.val"
"""

        
        