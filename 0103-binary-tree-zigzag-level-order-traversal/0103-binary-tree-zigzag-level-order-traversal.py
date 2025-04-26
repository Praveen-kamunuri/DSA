from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize a queue for level-order traversal.
        nodesQueue = deque()

        # Result list to store the final zigzag level order traversal
        result = []

        # If the tree is empty, return an empty list.
        if not root:
            return result

        # Start with the root node in the queue
        nodesQueue.append(root)

        # Flag to determine the direction of traversal
        left_to_right = True

        # Traverse the tree level by level
        while nodesQueue:
            # Number of nodes at the current level
            size = len(nodesQueue)

            # List to store the current level's values
            row = [0] * size

            # Process each node at the current level
            for i in range(size):
                # Pop a node from the front of the queue
                node = nodesQueue.popleft()

                # Determine the index for the current node value
                index = i if left_to_right else (size - 1 - i)

                # Place the node's value at the correct index in the row
                row[index] = node.val

                # Add the left child to the queue if it exists
                if node.left:
                    nodesQueue.append(node.left)

                # Add the right child to the queue if it exists
                if node.right:
                    nodesQueue.append(node.right)

            # Add the current level's row to the result
            result.append(row)

            # Toggle the direction for the next level
            left_to_right = not left_to_right

        return result

# Time Complexity: O(n)
# - Each node is visited exactly once, so the overall complexity is O(n),
#   where n is the number of nodes in the tree....

# Space Complexity: O(w)
# - The space required for the deque is proportional to the maximum width (w)
#   of the tree, which occurs at the largest level.
# - In the worst case, for a balanced binary tree, w ≈ n/2, so the space complexity is O(n)