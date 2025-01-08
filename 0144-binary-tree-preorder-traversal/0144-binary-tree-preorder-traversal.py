# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       
        # Initialize an empty list to store the traversal result
        ans = []

        # If the tree is empty, return an empty list
        if not root:
            return ans

        # Initialize a stack to keep track of nodes to visit
        stack = []
        stack.append(root)  # Start with the root node

        # Continue traversal while there are nodes in the stack
        while stack:
            # Pop the last node added to the stack
            node = stack.pop()

            # Visit the node by appending its value to the result list
            ans.append(node.val)

            # Preorder is Root -> Left -> Right
            # We push the right child first so that the left child is processed next
            if node.right:
                stack.append(node.right)

            # Push the left child onto the stack
            if node.left:
                stack.append(node.left)

        # Return the preorder traversal result.
        return ans


"""
        Iterative Preorder Traversal: Root -> Left -> Right

        Time Complexity (TC): O(n)
        - We visit each node exactly once.

        Space Complexity (SC): O(n)
        - In the worst case (skewed tree), the stack holds all n nodes.
        - In the best case (balanced tree), the stack holds O(log n) nodes.
        """