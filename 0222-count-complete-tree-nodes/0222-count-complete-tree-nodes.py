from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base case: If the tree is empty, return 0
        if not root:
            return 0

        # Function to calculate the height of the leftmost path in the tree
        def getLeftHeight(node):
            cnt = 0  # Initialize height counter
            while node:
                node = node.left  # Move left in the tree
                cnt += 1  # Increase height counter
            return cnt

        # Function to calculate the height of the rightmost path in the tree
        def getRightHeight(node):
            cnt = 0  # Initialize height counter
            while node:
                node = node.right  # Move right in the tree
                cnt += 1  # Increase height counter
            return cnt

        # Compute left and right subtree heights.
        left = getLeftHeight(root)
        right = getRightHeight(root)

        # If left and right heights are equal, it's a perfect binary tree
        if left == right:
            return (2 ** left) - 1  # Formula for total nodes in a perfect binary tree

        # If not a perfect tree, recursively count nodes in left and right subtrees
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


# Time Complexity (TC):
# - If the tree is a perfect binary tree, O(log N) height calculations are done in O(log N) time.
# - If the tree is not perfect, recursive calls lead to O(log N) recursive levels.
# - Each level performs O(1) work, leading to an overall worst-case time complexity of **O(log^2 N)**

# Space Complexity (SC):
# - The recursion depth in the worst case is O(log N), so the space complexity is **O(log N)**.
