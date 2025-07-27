import sys
import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build adjacency list (undirected graph)
        adj = [[] for _ in range(n)]
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))  # Undirected graph requires both directions

        # Step 2: Initialize distance and ways arrays
        distance = [sys.maxsize] * n  # Shortest distances from node 0
        ways = [0] * n                # Number of shortest paths to each node

        distance[0] = 0               # Distance to source node is 0
        ways[0] = 1                   # Only one way to reach source node: stay there

        mod_val = 10**9 + 7           # To avoid large numbers (standard CP modulo)

        # Step 3: Min-heap for Dijkstra's algorithm
        min_heap = []
        heapq.heappush(min_heap, (0, 0))  # (distance, node)

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            # Optimization: Skip if a better path to this node is already known
            if dist > distance[node]:
                continue

            for neighbour, edge_wt in adj[node]:
                new_dist = dist + edge_wt

                # Found a shorter path
                if new_dist < distance[neighbour]:
                    distance[neighbour] = new_dist
                    ways[neighbour] = ways[node]  # Reset count
                    heapq.heappush(min_heap, (new_dist, neighbour))

                # Found another shortest path (equal distance)
                elif new_dist == distance[neighbour]:
                    ways[neighbour] = (ways[neighbour] + ways[node]) % mod_val

        # Uncomment for debugging:
        # print("Distance array:", distance)

        return ways[n - 1] % mod_val  # Return count of shortest paths to destination node

# ============================
# ✅ Time Complexity:
# - Building the graph: O(M), where M = number of roads
# - Dijkstra's using min-heap: O(M * log N)
#   (Each edge may push/pull nodes in heap log N times)
# - Total: O((N + M) * log N)

# ✅ Space Complexity:
# - Adjacency list: O(N + M)
# - Distance and ways arrays: O(N)
# - Min-heap: O(N)

# Final: O(N + M) space
