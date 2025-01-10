# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize two stacks: stack1 for traversal and stack2 for storing the postorder result in reverse
        stack1 = []
        stack2 = []

        # Push the root node into stack1 to start the traversal
        stack1.append(root)

        # Traverse the tree
        while stack1:
            # Pop the top node from stack1
            node = stack1.pop()
            
            # Push the current node's value into stack2
            stack2.append(node.val)

            # Push the left child first to process it after the right child
            if node.left:
                stack1.append(node.left)

            # Push the right child
            if node.right:
                stack1.append(node.right)

        # Return the reversed stack2 to get the correct postorder traversal
        return stack2[::-1]

        # Time Complexity: O(n), where n is the number of nodes in the tree
        # Space Complexity: O(n), due to the usage of two stacks that can each hold up to n nodes in the worst case
