# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris Inorder Traversal:
        - Special type of inorder traversal that uses **O(1) extra space**.
        - It modifies tree temporarily (by linking predecessor), but restores it back.
        - No recursion, no stack → space-efficient!
        """
        
        inorder = []  # List to store inorder traversal
        curr = root  # Start from root

        while curr:  
            if curr.left is None:  
                # If no left child, visit the current node and move to right
                inorder.append(curr.val)
                curr = curr.right  
            else:
                # Finding inorder predecessor (rightmost node in left subtree)
                predecessor = curr.left  
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Establishing temporary link to current node
                    predecessor.right = curr
                    curr = curr.left  # Move left
                else:
                    # Breaking the temporary link (restoring tree)
                    predecessor.right = None
                    inorder.append(curr.val)  # Visit current node
                    curr = curr.right  # Move right
        
        return inorder

"""
\U0001f6e0️ **Time Complexity (TC)** → O(N)
   - Every node is visited at most **twice** (once during linking, once during restoration).
   - Hence, overall complexity remains **O(N)**.

\U0001f4cc **Auxiliary Space Complexity (ASC)** → O(1)
   - No extra stack or recursion.
   - Only modifies existing pointers temporarily, making it **constant space O(1)**.
"""
