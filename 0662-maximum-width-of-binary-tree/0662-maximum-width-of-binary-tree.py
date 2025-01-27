from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # If the root is null, the width is zero
        if not root:
            return 0
        
        # Initialize a variable to store the maximum width
        max_width = 0
        
        # Use deque for efficient popping from the front
        queue = deque([(root, 0)])
        
        # Perform level-order traversal
        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]  # Get the position of the first node in the level
            _, last_pos = queue[-1]  # Get the position of the last node in the level
            
            # Update max_width by calculating the width of the current level
            max_width = max(max_width, last_pos - first_pos + 1)
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node, pos = queue.popleft()
                
                # Add left child with updated position
                if node.left:
                    queue.append((node.left, 2 * pos))
                
                # Add right child with updated position
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
        
        return max_width
