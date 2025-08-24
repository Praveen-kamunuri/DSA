import sys
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list for the graph (1-based indexing)
        adj = [[] for _ in range(n + 1)]

        # Build the graph: u -> v with delay w...
        for u, v, delay in times:
            adj[u].append((v, delay))

        # Initialize distance to all nodes as infinity
        distance = [sys.maxsize] * (n + 1)
        distance[k] = 0  # Distance to starting node is 0

        # Min-heap priority queue to process nodes by minimum delay
        min_heap = [(0, k)]  # (delay, node)

        while min_heap:
            delay, node = heapq.heappop(min_heap)

            for neighbour, edge_wt in adj[node]:
                # Relaxation: check if new path is shorter
                if delay + edge_wt < distance[neighbour]:
                    distance[neighbour] = delay + edge_wt
                    heapq.heappush(min_heap, (distance[neighbour], neighbour))

        # Get the maximum delay among all reachable nodes
        res = max(distance[1:])  # Ignore index 0

        # Return -1 if any node is unreachable
        return -1 if res == sys.maxsize else res


# -------------------------------
# ✅ Time Complexity (TC):
# Building graph: O(E)
# Dijkstra (with heap): O((E + V) * log V)
# => Final TC = O(E * log V)

# ✅ Space Complexity (SC):
# - Adjacency list: O(E)
# - Distance array: O(V)
# - Min-heap: O(V)
# => Final SC = O(E + V)
# --------------------------------