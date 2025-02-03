from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # Step 1: Build parent map
        parent_map = {}
        
        def dfs(node, parent=None):
            if not node:
                return
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)

        # Step 2: BFS to find nodes at distance k
        queue = deque([(target, 0)])  # (node, current_distance)
        visited = set()
        result = []

        while queue:
            if queue[0][1] == k:  # If we reach level k, collect all nodes at thislevel
                return [node.val for node, _ in queue]

            for _ in range(len(queue)):  # Expand current level
                node, dist = queue.popleft()
                visited.add(node)

                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in visited:
                        queue.append((neighbor, dist + 1))

        return result
