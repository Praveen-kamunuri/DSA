# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs pre-order traversal of a binary tree.
        
        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: List of node values in pre-order traversal order.
        """

        # Initialize an empty list to store pre-order traversal result
        preOrder = []

        # Helper function to perform pre-order traversal
        def traversal(node):
            """
            Recursive function for pre-order traversal.
            
            Args:
            node (TreeNode): Current node being processed.
            """
            if node:  # Only process if the node is not None
                preOrder.append(node.val)  # Visit the current node
                traversal(node.left)       # Recur on the left subtree
                traversal(node.right)      # Recur on the right subtree

        # Start the traversal from the root node
        traversal(root)

        # Return the final pre-order traversal result
        return preOrder

# Time Complexity (TC):
# Each node is visited exactly once, and there are n nodes in the binary tree.
# Therefore, the time complexity is O(n).

# Space Complexity (SC):
# The space complexity is determined by the recursion stack.
# In the worst case (skewed tree), the recursion stack can go up to n levels, so SC = O(n).
# In the best case (balanced tree), the height is log(n), so SC = O(log n).
