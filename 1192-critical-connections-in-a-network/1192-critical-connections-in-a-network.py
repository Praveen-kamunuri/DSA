class Solution:
    def __init__(self):
        # Timer to keep track of discovery time during DFS
        self.timer = 1

    def dfs(self, node, parent, adj, tin, low, vis, bridges):
        # Mark the current node as visited
        vis[node] = 1

        # Set the discovery time and low-link value for this node
        tin[node] = low[node] = self.timer
        self.timer += 1  # Increment timer for next node

        # Explore all adjacent nodes
        for adj_node in adj[node]:
            if adj_node == parent:
                # Skip the parent node to avoid going back
                continue
            
            if vis[adj_node] == 0:
                # If the adjacent node is not visited, do DFS
                self.dfs(adj_node, node, adj, tin, low, vis, bridges)

                # After DFS call, update the low-link value for the current node
                low[node] = min(low[node], low[adj_node])

                # Check if the edge (node, adj_node) is a bridge
                # Condition: If the lowest reachable time from adj_node is greater than discovery time of node
                if low[adj_node] > tin[node]:
                    bridges.append([node, adj_node])
            
            else:
                # If the adjacent node is already visited and is not the parent
                # Then it's a back edge, update the low value of the current node
                low[node] = min(low[node], low[adj_node])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Intuition:
        ----------
        A critical connection (bridge) is an edge that, if removed, makes the graph disconnected.
        To find all such bridges, we use Tarjan's Algorithm:
        - Maintain two arrays:
          tin[node]: Discovery time of the node
          low[node]: Lowest discovery time reachable from that node
        - During DFS:
          If low[adj_node] > tin[node], then edge (node, adj_node) is a bridge.
        """

        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Step 2: Initialize helper arrays
        visited = [0] * n    # To mark visited nodes
        tin = [0] * n        # Discovery times
        low = [0] * n        # Lowest reachable discovery time
        bridges = []         # To store all bridges

        # Step 3: Call DFS starting from node 0
        # (In case of disconnected graph, run DFS for all unvisited nodes)
        self.dfs(0, -1, adj, tin, low, visited, bridges)

        return bridges


# ------------------------------
# Time Complexity:
# ------------------------------
# - Building adjacency list: O(n + E), where E = number of edges
# - DFS traversal: O(n + E) (each node and edge visited once)
# Overall: O(n + E)
#
# ------------------------------
# Space Complexity:
# ------------------------------
# - Adjacency list: O(n + E)
# - Arrays tin, low, visited: O(n)
# - Recursion stack: O(n)
# Overall: O(n + E)...
