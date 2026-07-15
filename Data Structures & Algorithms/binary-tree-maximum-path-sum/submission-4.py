# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]

        def dfs(root):
    
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            useable = max(root.val, 
                        root.val + left, 
                            root.val + right)

            max_sum[0] = max(max_sum[0], useable, (root.val + left + right))
            return useable

        dfs(root)
        return max_sum[0]

"""
solved this qn from scratch, 0 excuse to bottle in the future

we wish to find the max path sum
there are exponential num of paths, alr hints towards dp

for dp we need to identify the subproblems

given a tree at the root we want the max path sum, 
but this path may not involve the root

so now at a node we have to answer 2 qns:
    1) what is the max path if I am used by upper nodes
    2) what is the max path if I was the root

only the 1st qn's answer is required by other nodes to help compute answers to their 2 qns
and the  2nd qn's answer we can store and keep track if its the max we've ever seen

############################################################################################

so now answering the qns when we are at a particular node

1) what is the max path if I am used by upper nodes
    useable = max(root.val, 
                  root.val + left,
                  root.val + right)
    
    upper nodes can use the max of these values to help with their max path
    but cannot use 
    root.val + left + right, since thats no longer a "path" since it branches

2)  what is the max path if I was the root
    max path can either be
        - something we've seen before                    useable here means => paths upper nodes can use
        - one of the "useable" paths
        - root.val + left + right

    max_sum[0] = max(max_sum[0], useable, (root.val + left + right))
"""
        

            