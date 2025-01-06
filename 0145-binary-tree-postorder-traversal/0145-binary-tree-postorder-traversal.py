# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs post-order traversal of a binary tree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: List of node values in post-order traversal order.
        """

        # Initialize an empty list to store post-order traversal result
        postOrder = []

        # Helper function to perform post-order traversal
        def traversal(node):
            """
            Recursive function for post-order traversal.

            Args:
            node (TreeNode): Current node being processed.
            """
            if node:  # Only process if the node is not None
                traversal(node.left)      # Recur on the left subtree
                traversal(node.right)     # Recur on the right subtree
                postOrder.append(node.val)  # Visit the current node after its subtrees

        # Start the traversal from the root node
        traversal(root)

        # Return the final post-order traversal result
        return postOrder

# Time Complexity (TC):
# Each node is visited exactly once, and there are n nodes in the binary tree.
# Therefore, the time complexity is O(n).

# Space Complexity (SC):
# The space complexity is determined by the recursion stack.
# In the worst case (skewed tree), the recursion stack can go up to n levels, so SC = O(n).
# In the best case (balanced tree), the height is log(n), so SC = O(log n).
