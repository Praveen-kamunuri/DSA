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

        # Initialize two stacks: 
        # stack1 is used to traverse the tree
        # stack2 is used to store the postorder result in reverse
        stack1 = []
        stack2 = []

        # Start traversal by pushing the root node to stack1
        stack1.append(root)

        # Traverse the tree until stack1 is empty
        while stack1:
            # Pop the top node from stack1
            node = stack1.pop()

            # Push the node's value into stack2
            stack2.append(node.val)

            # Push the left child first (if exists) so that the right child
            # is processed first when reversing stack2
            if node.left:
                stack1.append(node.left)

            # Push the right child (if exists)
            if node.right:
                stack1.append(node.right)

        # Return the reversed stack2 to get the postorder traversal
        return stack2[::-1]

