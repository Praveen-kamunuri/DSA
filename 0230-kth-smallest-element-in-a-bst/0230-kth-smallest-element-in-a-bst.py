# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Counter to track the number of elements visited in inorder traversal
        self.cnt = 0  

        # Variable to store the kth smallest element
        self.result = None  

        # Inorder traversal function (Left -> Node -> Right)
        def inorder(root, k):
            if not root or self.result is not None:  
                return  # Stop recursion if we reach a null node or already found kth smallest

            inorder(root.left, k)  # Traverse the left subtree

            self.cnt += 1  # Increment counter as we visit a node

            # If counter matches k, store the result and stop further traversal
            if self.cnt == k:
                self.result = root.val
                return  # No need to continue further

            inorder(root.right, k)  # Traverse the right subtree

        inorder(root, k)  # Start inorder traversal from root

        return self.result  # Return the kth smallest element

"""
# Time Complexity (TC):
- The worst-case time complexity is **O(N)**, where N is the number of nodes.
- In the worst case, we traverse the entire tree.

# Space Complexity (SC):
- The space complexity is **O(H)**, where H is the height of the tree (recursive stack).
- Best case (balanced BST) -> O(log N), worst case (skewed tree) -> O(N).....
"""