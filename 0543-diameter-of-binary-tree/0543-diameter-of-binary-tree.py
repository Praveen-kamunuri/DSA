# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to keep track of the maximum diameter (number of edges in the longest path)
        self.maxi = 0

        # Helper function to calculate the height of a subtree
        def check_height(node):
            # Base case: if the node is None, the height is 0
            if not node:
                return 0

            # Recursively calculate the height of the left subtree
            left = check_height(node.left)

            # Recursively calculate the height of the right subtree
            right = check_height(node.right)

            # Update the maximum diameter by comparing the current diameter (left + right) with the existing maximum
            self.maxi = max(self.maxi, left + right)

            # Return the height of the current subtree
            # Height = 1 (for the current node) + max(left height, right height)
            return 1 + max(left, right)

        # Start the recursive process from the root node.
        check_height(root)

        # Return the maximum diameter calculated.
        return self.maxi

        # Time Complexity (TC): O(n), where n is the number of nodes in the tree.
        # We visit each node once to calculate its height and update the diameter.

        # Space Complexity (SC): O(h), where h is the height of the tree.
        # This is the space used by the recursion stack in the worst case (skewed tree).
