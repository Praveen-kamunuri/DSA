# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not root:
            return []
        
        parent_map = {}  # Stores parent pointers for each node
        
        # DFS to map each node to its parent
        def dfs(node, parent=None):
            if not node:
                return 
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)  # Build parent mapping

        result = []  # Stores nodes at distance K
        visited = set()  # Tracks visited nodes
        q = deque([(target, 0)])  # Queue for BFS (node, distance)

        while q:
            if q[0][1] == k:  # If front node's distance is K, collect results
                return [node.val for node, dist in q]

            for i in range(len(q)):  # Process current level
                node, dist = q.popleft()
                visited.add(node)

                # Explore left, right, and parent nodes
                for neighbour in (node.left, node.right, parent_map[node]):
                    if neighbour and neighbour not in visited:
                        q.append((neighbour, dist + 1))

        return result  # Return empty if no nodes found at distance K


"""
Time Complexity: O(N)
- The DFS to build the parent map takes O(N).
- The BFS traversal also runs in O(N) in the worst case.

Space Complexity: O(N)
- The parent_map stores O(N) nodes.
- The queue in BFS can grow up to O(N).
- The visited set also stores O(N) nodes.
""" 
