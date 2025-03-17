from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key from the BST and maintains BST properties.

        Parameters:
        root (TreeNode): The root of the BST.
        key (int): The value to be deleted.

        Returns:
        TreeNode: The root of the modified BST.
        """
        
        # If root is None, return None (base case)
        if not root:
            return None

        # If the root itself is the node to be deleted, handle deletion separately
        if root.val == key:
            return self.helper(root)

        dummy = root  # Store the reference to the original root

        while root:
            if root.val > key:  # Move to the left subtree if key is smaller
                if root.left and root.left.val == key:
                    # If left child is the target node, delete it using helper
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left  # Keep searching in the left subtree
            else:  # Move to the right subtree if key is greater
                if root.right and root.right.val == key:
                    # If right child is the target node, delete it using helper
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right  # Keep searching in the right subtree

        return dummy  # Return the modified tree

    def helper(self, root: TreeNode) -> Optional[TreeNode]:
        """
        Handles deletion cases when the target node is found.
        1. If the node has no left child, return the right child.
        2. If the node has no right child, return the left child.
        3. If the node has both left and right children:
            - Find the rightmost node in the left subtree.
            - Attach the right subtree to this rightmost node.
            - Return the left subtree as the new root of this subtree.
        """
        if root.left is None:
            return root.right  # Replace the deleted node with its right child
        elif root.right is None:
            return root.left  # Replace the deleted node with its left child

        # If both left and right children exist
        right_child = root.right  # Store the right subtree
        last_right = self.find_last_right(root.left)  # Find the rightmost node in the left subtree
        last_right.right = right_child  # Attach the original right subtree to this node

        return root.left  # Return the modified left subtree as new root

    def find_last_right(self, root: TreeNode) -> TreeNode:
        """
        Finds the rightmost node in a subtree.

        Parameters:
        root (TreeNode): The root of the subtree.

        Returns:
        TreeNode: The rightmost node in the subtree.
        """
        while root.right:
            root = root.right
        return root

"""
Time Complexity (TC):
- Searching for the node to delete: O(h) in a BST (h = height of the tree).
- Finding the rightmost node of the left subtree: O(h).
- Modifying pointers: O(1).
- Overall: O(h), where h is the height of the tree.
  - Best case (Balanced BST): O(log N)
  - Worst case (Skewed BST): O(N)

Space Complexity (SC):
- Iterative approach with no extra data structures: O(1) auxiliary space.
- Recursive calls (in helper and find_last_right): O(h) recursion stack.
  - Best case (Balanced BST): O(log N)
  - Worst case (Skewed BST): O(N)
"""
