# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST).
        
        Parameters:
        root (TreeNode): The root of the BST.
        p (TreeNode): First target node.
        q (TreeNode): Second target node.
        
        Returns:
        TreeNode: The LCA of nodes p and q.
        """

        # Base case: If the root is None, return None
        if root is None:
            return None

        # Get the value of the current node..
        curr = root.val

        # If both p and q are greater than current node, LCA lies in the right subtree
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are smaller than current node, LCA lies in the left subtree
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If one node is on the left and the other on the right (or one is the root itself), 
        # then the current node is the LCA
        return root

"""
Time Complexity: O(h)
- In the worst case, we traverse the height of the tree.
- In a balanced BST, the height h is O(log n), so the complexity is O(log n).
- In an unbalanced BST (skewed tree), h can be O(n), making the complexity O(n).

Space Complexity: O(h)
- Due to recursive calls, the function stack can go up to O(h).
- In a balanced BST, this is O(log n).
- In an unbalanced BST, this is O(n).
"""
