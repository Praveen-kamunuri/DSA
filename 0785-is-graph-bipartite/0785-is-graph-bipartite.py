class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means unvisited

        # DFS function to color nodes...
        def dfs(node, c):
            color[node] = c  # Assign color to current node
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Recursively color neighbor with opposite color
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    # If neighbor already has same color → Not bipartite
                    return False
            return True

        # Go through all nodes in case graph is disconnected
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):  # Start DFS with color 0
                    return False

        return True

# -----------------------------
# Time Complexity: O(V + E)
#   - Each node and edge is visited once in DFS.
# Space Complexity: O(V)
#   - color[] array + recursive call stack in worst case.
# -----------------------------
