class Solution:
    def __init__(self):
        # Timer is used to assign discovery time for each node
        self.timer = 1

    def dfs(self, node, parent, visited, adj, tin, low, bridges):
        # Mark the current node as visited
        visited[node] = 1

        # Initialize tin (discovery time) and low (lowest reachable time)
        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1  # Increment timer for next node

        # Explore all neighbors of the current node
        for neighbour in adj[node]:
            if neighbour == parent:
                # Skip the parent node to avoid going back
                continue

            if visited[neighbour] == 0:
                # DFS on unvisited neighbor
                self.dfs(neighbour, node, visited, adj, tin, low, bridges)

                # After DFS, update the low-link value of the current node
                low[node] = min(low[node], low[neighbour])

                # Check if the edge (node, neighbour) is a bridge
                # If the lowest reachable vertex from neighbour is greater than discovery time of node,
                # then this edge is critical
                if low[neighbour] > tin[node]:
                    bridges.append((neighbour, node))
            else:
                # If neighbor is already visited and is not the parent,
                # it's a back edge, so update low[node]
                low[node] = min(low[node], low[neighbour])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Intuition:
        ----------
        A critical connection (bridge) is an edge that, if removed, disconnects the graph.
        We use Tarjan's Algorithm with DFS to find all bridges in the graph.
        The key idea:
        - Maintain discovery time (tin) and low-link values (low).
        - If for an edge (u, v), low[v] > tin[u], then (u, v) is a bridge.

        Approach:
        ---------
        1. Build adjacency list from the given edge list.
        2. Use DFS to visit nodes and compute tin and low values.
        3. Whenever low[neighbour] > tin[node], the edge is a bridge.
        """

        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Initialize helper arrays
        visited = [0] * n    # Track visited nodes
        tin = [0] * n        # Discovery time for each node
        low = [0] * n        # Lowest reachable time for each node
        bridges = []         # Store bridges

        # Step 3: Call DFS from node 0 (or all nodes for disconnected graphs)
        self.dfs(0, -1, visited, adj, tin, low, bridges)

        return bridges


# ------------------------------
# Time Complexity:
# ------------------------------
# Building adjacency list: O(n + E), where E = number of edges
# DFS traversal: O(n + E) because we visit each node and edge once
# Overall: O(n + E)
#
# ------------------------------
# Space Complexity:
# ------------------------------
# Adjacency list: O(n + E)
# Arrays tin, low, visited: O(n)
# Recursion stack: O(n)
# Overall: O(n + E)
