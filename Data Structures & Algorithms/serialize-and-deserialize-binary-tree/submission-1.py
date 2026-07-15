# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = data.split(",")
        self.i = 0

        def dfs():
            if nums[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(nums[self.i]))
            self.i += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()

"""
encode:
go in preorder traversal and add each str(node.val) to string
preorder is (root, left, right)

the reason why only preorder is enough is because we also add null nodes
so just preorder is needed to rebuild tree

decode:
instead of going element by element in the string and making a node for each
we recursively rebuild the tree (this is better cuz thats how we serialized the tree !)

we start from index 0
if its "N", we return None
if its not "N", we build the node
then increment index 
node.left = dfs()
node.right = dfs()

##########################################################################

You don't need a self.i >= len(nums) check
because your tree structure is guaranteed by the serialization process.

If your tree has N total nodes (including the null markers), 
the dfs function will be called exactly N times.

Each call consumes exactly one item from nums to 
determine if it should create a node or return None.

Since your nums list contains exactly the sequence 
needed to form that specific tree, the recursion 
will exhaust the list exactly as the last branch is closed.
"""


