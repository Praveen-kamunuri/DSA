from typing import Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Inserts a new value into the BST while maintaining BST properties.
        """

        def find_place(root, val):
            """
            Finds the correct position in the BST where the new node should be inserted
            Args:
                root (TreeNode): The root of the BST.
                val (int): The value to be inserted.
            Returns:
                TreeNode: The parent node where the new value should be attached
            """

            curr = root
            prev = None  # Keeps track of the parent node

            while curr:
                prev = curr  # Update the parent node before moving further
                
                # Move left if val is smaller, else move right
                if val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right

            return prev  # Returns the last non-null node (parent of the new node)

        # If the tree is empty, return a new node as root
        if not root:
            return TreeNode(val)

        # Find the parent node where the new value should be inserted
        insert_pos = find_place(root, val)

        # Create a new node with the given value
        new_node = TreeNode(val)

        # Attach the new node to the correct position.
        if val < insert_pos.val:
            insert_pos.left = new_node
        else:
            insert_pos.right = new_node

        return root  # Return the root of the modified BST


"""
Time Complexity (TC):
- O(log N) in a balanced BST (average case)
- O(N) in a skewed BST (worst case)

Space Complexity (SC):
- O(1) as we are using only a few extra variables (prev, curr, new_node)
- No additional recursive calls or extra space used
"""