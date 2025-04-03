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
        """
        Computes the maximum width of a binary tree. The width of a level is defined as 
        the number of nodes between the leftmost and rightmost non-null nodes at that level
        """
        
        if not root:
            return 0  # If the tree is empty, width is 0
        
        q = deque([(root, 0)])  # Queue stores pairs of (node, position_index)
        max_width = 0  # Variable to track the maximum width
        
        while q:
            size = len(q)  # Number of nodes at the current level
            
            first_node, first_pos = q[0]  # Get position of leftmost node in the level.
            last_node, last_pos = q[-1]   # Get position of rightmost node in the level
            
            # Update max width
            max_width = max(max_width, last_pos - first_pos + 1)
            
            for _ in range(size):
                node, pos = q.popleft()  # Dequeue node and its position
                
                # Assign positions to children as per 0-based indexing:
                if node.left:
                    q.append((node.left, 2 * pos + 1))  # Left child -> 2 * pos + 1
                if node.right:
                    q.append((node.right, 2 * pos + 2))  # Right child -> 2 * pos + 2
        
        return max_width  # Return the maximum width found

# Time Complexity: O(N), where N is the number of nodes in the tree.
#   - Each node is visited once during the BFS traversal.
# Space Complexity: O(N), due to storing nodes in the queue at the widest level.
