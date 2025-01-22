from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # If the tree is empty, it is symmetric
        if not root:
            return True

        # Helper function to check if two subtrees are mirror images of each other
        def is_mirror(t1, t2):

            # If both nodes are None, they are symmetric
            if not t1 and not t2:
                return True

            # If only one node is None, trees are not symmetric
            if not t1 or not t2:
                return False

            # Check if current nodes have the same value and recursively compare 
            # left subtree of t1 with right subtree of t2 and 
            # right subtree of t1 with left subtree of t2
            return (t1.val == t2.val and 
                    is_mirror(t1.left, t2.right) and 
                    is_mirror(t1.right, t2.left))

        # Compare the left and right subtrees of the root
        return is_mirror(root.left, root.right)

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree (O(n) in the worst case for skewed trees).
