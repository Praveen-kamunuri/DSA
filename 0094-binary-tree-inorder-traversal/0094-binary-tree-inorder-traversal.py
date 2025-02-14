

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        '''
        # Special inorder traversal called Morris Inorder Traversal
        # This method uses no extra space and modifies the tree temporarily.

        '''
        result = []  # Stores the inorder traversal result
        curr = root  # Pointer to traverse the tree

        while curr:
            if curr.left is None:
                # If there is no left child, visit the node and move to the right
                result.append(curr.val)
                curr = curr.right
            else:
                # Find the inorder predecessor (rightmost node in left subtree)
                predecesor = curr.left
                while predecesor.right and predecesor.right != curr:
                    predecesor = predecesor.right

                if predecesor.right is None:
                    # Create a temporary link to the current node
                    predecesor.right = curr
                    curr = curr.left  # Move to the left subtree
                else:
                    # Revert the changes (restore the original tree)
                    predecesor.right = None
                    result.append(curr.val)  # Visit the node
                    curr = curr.right  # Move to the right subtree

        return result  # Return the inorder traversal result

# Time Complexity: O(N) - Each node is visited at most twice.
# Space Complexity: O(1) - No extra space is used, as Morris traversal modifies the tree temporarily.
