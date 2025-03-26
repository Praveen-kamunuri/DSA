# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        This function finds the maximum path sum in a binary tree.
        A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
        The path must contain at least one node and does not need to go through the root
        """

        # Helper function to calculate the maximum path sum starting from a given node.
        # It also updates the overall maximum path sum found so far.
        def find_max_sum_path(node, maxi):
            if not node:
                # If the current node is None, return 0 as the path sum.
                return 0

            # Recursively calculate the maximum path sum for the left subtree.
            # If the left path sum is negative, we ignore it (hence max(0, ...)).
            left = max(0, find_max_sum_path(node.left, maxi))

            # Recursively calculate the maximum path sum for the right subtree.
            # If the right path sum is negative, we ignore it.
            right = max(0, find_max_sum_path(node.right, maxi))

            # Update the overall maximum path sum if the current path (left + right + node's value).
            # is greater than the previously recorded maximum path sum.
            maxi[0] = max(maxi[0], left + right + node.val)

            # Return the maximum path sum starting from the current node,
            # considering either the left or right subtree, plus the current node's value.
            return max(left, right) + node.val

        # Initialize the maximum path sum as negative infinity to handle negative values in the tree.
        maxi = [float('-inf')]

        # Start the helper function from the root node.
        find_max_sum_path(root, maxi)

        # Return the overall maximum path sum found.
        return maxi[0]

# ---------------------------
# Time Complexity (TC):
# O(n), where n is the number of nodes in the binary tree.
# This is because we traverse each node once to calculate the maximum path sum.

# Space Complexity (SC):
# O(h), where h is the height of the binary tree.
# The space complexity is determined by the recursive stack, which can go as deep as the height of the tree.
# In the worst case (skewed tree), the height can be n (O(n) space), and in the best case (balanced tree), it is O(log n).
