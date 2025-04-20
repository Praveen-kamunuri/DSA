# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Recovers a BST where two nodes were swapped by mistake.
        This is done using inorder traversal and without modifying the structure.
        """

        # These will store the misplaced nodes
        self.first = self.middle = self.last = self.prev = None

        def inorder(node):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Detect swapped nodes
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    # First violation
                    self.first = self.prev
                    self.middle = node
                else:
                    # Second violation
                    self.last = node

            # Move prev to current node
            self.prev = node

            # Traverse right subtree
            inorder(node.right)

        # Perform the inorder traversal to find misplaced nodes
        inorder(root)

        # Swap the values to fix the tree
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val

"""
Time Complexity: O(n)
- We visit each node exactly once in the inorder traversal.

Space Complexity: O(h)
- h is the height of the tree due to recursion stack.
- h = log(n) for balanced trees, up to h = n for skewed trees.
"""
