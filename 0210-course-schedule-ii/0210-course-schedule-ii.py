class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Helper DFS function to detect cycle and build topological order
        def is_cycle(node, adj, visited, path_sum, n, result):

            visited[node] = 1         # Mark node as visited
            path_sum[node] = 1        # Mark node as part of current DFS path (for cycle detection)

            for neighbour in adj[node]:
                if visited[neighbour] != 1:
                    # Recurse DFS
                    if is_cycle(neighbour, adj, visited, path_sum, n, result) == False:
                        return False  # Cycle found in child
                elif path_sum[neighbour] == 1:
                    return False      # Cycle found (back edge)

            path_sum[node] = 0        # Remove node from current path
            result.append(node)       # Append after processing all children (post-order)
            return True               # No cycle from this node

        # Step 1: Build adjacency list
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)  # b → a (you must take b before a)

        # Step 2: Prepare visited and path trackers
        visited = [0] * numCourses
        path_sum = [0] * numCourses
        result = []

        # Step 3: Perform DFS from each unvisited node
        for i in range(numCourses):
            if visited[i] != 1:
                if is_cycle(i, adj, visited, path_sum, numCourses, result) == False:
                    return []  # Cycle detected → not possible to finish all courses

        return result[::-1]  # Reverse to get correct topological order..

# -------------------------------
# Time Complexity (TC): O(V + E)
# - V = numCourses
# - E = number of prerequisite pairs
# - Each node and edge is visited once

# Space Complexity (SC): O(V + E)
# - adj list takes O(E)
# - visited, path_sum arrays take O(V)
# - recursion stack can go up to O(V) depth in worst case
# -------------------------------
