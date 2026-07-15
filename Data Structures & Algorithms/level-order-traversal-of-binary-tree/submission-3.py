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
