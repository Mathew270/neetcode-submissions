# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def dfs(root):
            if not root:
                return 0
            
            right, left = dfs(root.right), dfs(root.left)
            res[0] = max(res[0], right + left)
            height = 1 + max(right, left)

            return height
        
        dfs(root)
        return res[0]

"""
we need to check the diameter at each root and keep track of the max

we do this by keeping track of the height, at each node
then to calculate the diameter at a node we add right height + left height
as that is what is returned by the dfs(right), dfs(left)

so essentially this is just a modified height recursion qn where we also keep track of 
res = max(res[0], right + left)

res is a list with one element to bypass local variable ref error


"""