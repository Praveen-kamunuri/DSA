class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Helper function to perform DFS and check for cycles
        def cycle_check(ind, adj, visited, path_sum):
            visited[ind] = 1        # Mark node as visited
            path_sum[ind] = 1       # Mark node in current DFS path

            for neighbour in adj[ind]:  # Visit all adjacent nodes
                # If the neighbor hasn't been visited yet, do DFS
                if visited[neighbour] != 1:
                    if cycle_check(neighbour, adj, visited, path_sum):
                        return True  # Cycle found
                # If the neighbor is already in the current path, cycle exists
                elif path_sum[neighbour] == 1:
                    return True

            path_sum[ind] = 0  # Backtrack - remove node from current path
            return False       # No cycle from this node

        # Step 1: Build adjacency list for the graph
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)  # To take course 'a', you must complete 'b' first

        # Step 2: Arrays to track visited nodes and current DFS path
        visited = [0] * numCourses   # 0 = unvisited, 1 = visited
        path_sum = [0] * numCourses  # 1 = part of current DFS call stack

        # Step 3: DFS from every unvisited node
        for i in range(numCourses):
            if visited[i] != 1:
                if cycle_check(i, adj, visited, path_sum):
                    return False  # Cycle detected → cannot finish all courses

        return True  # No cycle found → all courses can be completed..


# --------------------------------------------
# ✅ Time Complexity (TC):
# - Building adj list: O(P), where P = len(prerequisites)
# - DFS for all nodes: O(N + P), where N = numCourses
# So overall: O(N + P)

# ✅ Space Complexity (SC):
# - adj list: O(N + P)
# - visited and path_sum arrays: O(N)
# - Call stack for DFS: O(N) in worst case (if all nodes are in one chain)
# So overall: O(N + P)

# Example:
# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]
# Output: False (cycle exists)
