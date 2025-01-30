from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([(root, 0)])

        max_width = 0

        while q:
            size = len(q)

            first_node, first_pos = q[0]

            last_node, last_pos = q[-1]

            max_width = max(max_width, last_pos - first_pos + 1)

            for i in range(size):

                node, pos = q.popleft()

                if node.left:
                    q.append((node.left, 2 * pos + 1))

                if node.right:
                    q.append((node.right, 2 * pos + 2))

        return max_width


        


        