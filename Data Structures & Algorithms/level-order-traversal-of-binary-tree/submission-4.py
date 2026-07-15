# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        #visited = set()
        q = deque()
        q.append(root)
        #visited.add(root)

        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                #visited.add(node)
                if node.left: #and node.left not in visited:
                    q.append(node.left)
                if node.right: #and node.right not in visited:
                    q.append(node.right)
            res.append(curr)

        return res

"""
res.append(curr)
this line here means that we append the list pointed to by curr to res
not that we append the pointer curr

we dont need to do curr[:] or anything
since we append the list
then in the next iteration we reassign curr to [], append stuff,
then append curr to res again

we are not appending the variable curr, but rather the list pointed by it
"""