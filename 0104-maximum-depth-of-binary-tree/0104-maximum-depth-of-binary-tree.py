# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None, the tree is empty, so the depth is 0.
        if root == None:
            return 0

        # Recursively find the depth of the left subtree.
        left = self.maxDepth(root.left)

        # Recursively find the depth of the right subtree.
        right = self.maxDepth(root.right)

        # Return 1 (for the current node) plus the maximum depth of the left and right subtrees.
        return 1 + max(left, right)

"""
Time Complexity: O(n)
- We visit each node once, where n is the number of nodes in the tree.

Space Complexity: O(h)
- The space complexity is determined by the recursive call stack.
- In the worst case (for a skewed tree), the height of the tree h can be n.
- In the best case (for a balanced tree), the height is log(n).
"""
