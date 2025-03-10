# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the binary tree into a linked list in-place.
        """

        curr = root

        while curr:
            # If there is a left subtree, we need to move it to the right
            if curr.left is not None:
                prev = curr.left

                # Find the rightmost node of the left subtree..
                while prev.right:
                    prev = prev.right

                # Connect the rightmost node of left subtree to the current right subtree
                prev.right = curr.right

                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None  # Remove reference to the left subtree

            # Move to the next right node.
            curr = curr.right

"""
Time Complexity: O(N), where N is the number of nodes in the tree.
- Each node is visited once, and finding the rightmost node of a subtree takes O(1) amortized time per node.

Space Complexity: O(1), since the transformation is done in-place without extra space.
"""
