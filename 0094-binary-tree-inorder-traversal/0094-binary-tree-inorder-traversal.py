# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        inOrder = []

        def traversal(node):

            if node:

                traversal(node.left)
                inOrder.append(node.val)
                traversal(node.right)

        traversal(root)

        return inOrder 
        