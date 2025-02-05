# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either preorder or inorder is empty, return None
        if not preorder and not inorder:
            return None

        # The first element of preorder is the root of the tree
        root_val = preorder[0]
        root = TreeNode(root_val)  # Create the root node

        # Find the index of the root value in inorder to separate left and right subtrees
        mid = inorder.index(root_val)

        # Recursively build the left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # Recursively build the right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the constructed tree
        return root

# Time Complexity (TC):
# - Finding the root in inorder takes O(N) time for each node.
# - For N nodes, this results in O(N^2) time complexity in the worst case.

# Space Complexity (SC):
# - O(N) space for the recursion stack in the worst case (when the tree is skewed).