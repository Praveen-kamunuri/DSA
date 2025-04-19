# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack to store the path to the next smallest node
        self.stack = []
        # Initialize the stack with the leftmost path from the root
        self.left_most_inorder(root)

    def left_most_inorder(self, node):
        # Go as left as possible and push all nodes along the way
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node from the stack (smallest unvisited node)
        top_node = self.stack.pop()

        # If the node has a right child, process its leftmost path
        if top_node.right:
            self.left_most_inorder(top_node.right)

        # Return the node's value
        return top_node.val

    def hasNext(self) -> bool:
        # Return True if there are still nodes to visit
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Time Complexity:
# - next(): O(1) on average (amortized), worst case O(h) where h = height of tree
# - hasNext(): O(1)

# Space Complexity:
# - O(h) where h is the height of the BST (due to the stack storing the path)
