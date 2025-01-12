# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate height and check if the tree is balanced.
        def check_height(node):
            # Base case: If the node is None, its height is 0.
            if not node:
                return 0

            # Recursively check the height of the left subtree.
            left_height = check_height(node.left)
            # If left subtree is unbalanced, propagate -1 upwards.
            if left_height == -1:
                return -1

            # Recursively check the height of the right subtree.
            right_height = check_height(node.right)
            # If right subtree is unbalanced, propagate -1 upwards.
            if right_height == -1:
                return -1

            # Check if the current node is balanced.
            # The difference between the heights of left and right subtrees should not exceed 1.
            if abs(left_height - right_height) > 1:
                return -1  # Tree is unbalanced.

            # If balanced, return the height of the current subtree.
            return max(left_height, right_height) + 1

        # Call the helper function on the root. If it returns -1, the tree is unbalanced.
        return check_height(root) != -1

"""
Time Complexity: O(n)
- Each node in the tree is visited once to calculate its height and check balance.
- Thus, the time complexity is proportional to the number of nodes, n.

Space Complexity: O(h)
- The space complexity is determined by the height of the recursive call stack.
- In the worst case (skewed tree), the height h can be n.
- In the best case (balanced tree), h is log(n).
"""
