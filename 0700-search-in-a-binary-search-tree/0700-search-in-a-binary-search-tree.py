from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        This function searches for a given value in a Binary Search Tree (BST).
        If the value exists, it returns the subtree rooted at that node.
        Otherwise, it returns None.
        """

        def find(root, val):
            """
            Iteratively searches for a node containing 'val' in the BST.
            If found, returns the node; otherwise, returns None.
            """
            while root:
                if val == root.val:
                    return root  # Node found, return the subtree root
                
                elif val > root.val:
                    root = root.right  # Search in the right subtree
                
                else:
                    root = root.left  # Search in the left subtree
            
            return None  # Value not found

        return find(root, val)  # Return the found node or None if not found


# Time Complexity: O(H), where H is the height of the BST.
#   - Best case: O(log N) for a balanced BST.
#   - Worst case: O(N) for a skewed BST (linked list-like structure).

# Space Complexity: O(1) 
#   - No extra space is used, as we are implementing an iterative search.

                