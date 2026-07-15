# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []

        if not root:
            return []

        while q:
            temp = []
            for i in range(len(q)):
                element = q.popleft()
                temp.append(element.val)

                if element.left:
                    q.append(element.left)

                if element.right:
                    q.append(element.right)

            res.append(temp[-1])

        return res