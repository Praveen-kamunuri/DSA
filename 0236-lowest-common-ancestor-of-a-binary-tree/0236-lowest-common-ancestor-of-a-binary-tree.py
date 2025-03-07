# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Function to find the lowest common ancestor (LCA) of two given nodes in a binary tree.

        Args:
        root (TreeNode): The root of the binary tree.
        p (TreeNode): The first target node.
        q (TreeNode): The second target node

        Returns:
        TreeNode: The lowest common ancestor of nodes p and q.
        """

        # Base case: If root is None or root matches either p or q, return root
        if not root or root == p or root == q:
            return root

        # Recursively search for LCA in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees, root is their LCA
        if left and right:
            return root
        
        # If one side is None, return the other (either left or right subtree has both nodes)
        return left if left else right

"""
Time Complexity (TC): 
- O(N), where N is the number of nodes in the binary tree.
- Each node is visited once in a recursive depth-first search.

Space Complexity (SC): 
- O(H), where H is the height of the tree due to recursive call stack.
- In the worst case (skewed tree), H = O(N).
- In the best case (balanced tree), H = O(log N).
"""
