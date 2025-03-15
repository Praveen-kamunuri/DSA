from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the result of level-order traversal.
        ans = []
        
        # If the root is None (empty tree), return an empty list
        if not root:
            return ans

        # Initialize a queue to perform level-order traversal
        q = deque()
        q.append(root)  # Add the root node to the queue.
        
        # Loop until the queue is empty
        while q:
            size = len(q)  # Get the number of nodes at the current level
            level = []  # List to store nodes' values at the current level
            
            # Process all nodes at the current level
            for i in range(size):
                node = q.popleft()  # Remove the front node from the queue
                level.append(node.val)  # Add the node's value to the current level list
                
                # If the node has a left child, add it to the queue
                if node.left:
                    q.append(node.left)
                
                # If the node has a right child, add it to the queue
                if node.right:
                    q.append(node.right)
            
            # Add the current level's values to the result.
            ans.append(level)
        
        # Return the list of all levels
        return ans

# Time Complexity (TC):
# - Each node is visited exactly once.
# - Appending to the list and adding/removing from the deque are O(1) operations.
# - Therefore, the overall time complexity is O(N), where N is the number of nodes in the binary tree.

# Space Complexity (SC):
# - The space complexity is determined by the maximum size of the queue. 
# - In the worst case (a completely balanced binary tree), the queue will store all the nodes of the last level, which is approximately N/2.
# - Hence, the space complexity is O(N) for the queue.
# - Additionally, the space for storing the result list `ans` is also O(N).
# - Thus, the overall space complexity is O(N).