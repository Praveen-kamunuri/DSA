# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        self.index = 0  # Tracks current index in the preorder list

        # Helper function to build BST with an upper bound constraint
        def helper(bound = float('inf')):
            # If all elements are used or current value exceeds the bound, return None
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None

            # Take the current value as root node's value
            root_val = preorder[self.index]
            self.index += 1  # Move to the next index

            # Create a new tree node with root_val
            root = TreeNode(root_val)

            # All values for the left subtree must be less than root_val
            root.left = helper(root_val)

            # All values for the right subtree must be less than 'bound'
            root.right = helper(bound)

            return root

        # Call helper starting with infinite bound (root has no limit)
        return helper()


# Time Complexity: O(n), where n is the number of nodes in the preorder list.
# Each node is visited exactly once.

# Space Complexity: O(n) in the worst case due to recursion stack (when tree is skewed),
# and O(log n) in the best case (balanced tree).
