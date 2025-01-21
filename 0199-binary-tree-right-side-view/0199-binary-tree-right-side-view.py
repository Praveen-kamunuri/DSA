from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # List to store the right side view elements
        self.ds = []

        # Reverse Preorder DFS (Root -> Right -> Left)
        def dfs_rev_preorder(node, level):
            # Base case: If node is None, return
            if not node:
                return

            # If the current level is equal to the number of elements in the list,
            # it means this is the first node encountered at this depth (rightmost node)
            if level == len(self.ds):
                self.ds.append(node.val)

            # Explore the right subtree first to prioritize rightmost nodes
            if node.right:
                dfs_rev_preorder(node.right, level + 1)

            # Then explore the left subtree
            if node.left:
                dfs_rev_preorder(node.left, level + 1)

        # Start DFS from the root at level 0
        dfs_rev_preorder(root, 0)

        # Return the right-side view of the binary tree.
        return self.ds 

# Time Complexity: O(n), where n is the number of nodes in the tree. 
# Each node is visited once.

# Space Complexity: O(h), where h is the height of the tree. 
# In the worst case (skewed tree), the space complexity is O(n).
# In the best case (balanced tree), the space complexity is O(log n).
