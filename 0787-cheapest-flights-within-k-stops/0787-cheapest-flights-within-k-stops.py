import sys
from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build adjacency list from flights
        adj = [[] for _ in range(n)]
        for u, v, wt in flights:
            adj[u].append((v, wt))  # edge from u to v with weight wt

        # Step 2: Initialize distance array with infinity
        distance = [sys.maxsize] * n
        distance[src] = 0  # cost to reach source is 0

        # Step 3: Initialize queue for BFS: (number of stops, (current node, current cost))
        q = deque()
        q.append((0, (src, 0)))  # 0 stops, at source, with 0 cost

        # Step 4: Perform BFS with stop constraint.
        while q:
            stops, node_with_cost = q.popleft()
            node = node_with_cost[0]
            cost = node_with_cost[1]

            # If stops exceeded k, skip further exploration
            if stops > k:
                continue

            # Explore neighbors
            for neighbour, wt in adj[node]:
                if cost + wt < distance[neighbour] and stops <= k:
                    distance[neighbour] = cost + wt
                    q.append((stops + 1, (neighbour, cost + wt)))

        # Step 5: If destination is unreachable, return -1.
        if distance[dst] == sys.maxsize:
            return -1
        else:
            return distance[dst]

# -------------------------------
# Time Complexity: O(n + E * k)
# - In worst case, each edge is visited at most k times
# - So total operations: O(E * k)
#
# Space Complexity: O(n + E)
# - Adjacency list: O(E)
# - Distance array: O(n)
# - Queue: up to O(n * k) in worst case