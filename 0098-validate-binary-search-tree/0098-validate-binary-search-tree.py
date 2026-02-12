import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        A valid BST is defined as:
          - The left subtree of a node contains only nodes with keys less than the node's key.
          - The right subtree of a node contains only nodes with keys greater than the node's key.
          - Both the left and right subtrees must also be binary search trees...
        """

        def is_valid_bst(node, min_val, max_val):
            """
            Recursively validates the BST.
            - node: current tree node
            - min_val: the lower bound for the current node value
            - max_val: the upper bound for the current node value
            """
            # Base case: An empty node/subtree is valid.
            if node is None:
                return True

            # Check if the current node's value violates the BST property.
            if node.val >= max_val or node.val <= min_val:
                return False

            # Recursively validate the left and right subtrees with updated bounds.
            # For the left subtree, the maximum allowed value is node.val.
            # For the right subtree, the minimum allowed value is node.val.
            return (is_valid_bst(node.left, min_val, node.val) and 
                    is_valid_bst(node.right, node.val, max_val))

        # Initialize the recursion with the lowest and highest possible values.
        # Using sys.maxsize for a practical limit (Python ints are arbitrary precision).
        return is_valid_bst(root, -sys.maxsize - 1, sys.maxsize)

# TC: O(n) - We traverse each node exactly once.
# SC: O(n) in the worst-case (unbalanced tree) due to recursion stack, O(log n) for balanced trees...