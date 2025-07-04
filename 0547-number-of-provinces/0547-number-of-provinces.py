class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Total number of cities.
        n = len(isConnected)

        # Count of connected components (provinces)..
        provinces = 0

        # Keeps track of visited cities
        visited = [False] * n

        # Depth-First Search (DFS) to explore all cities connected to 'city'
        def dfs(city):
            for neighbour in range(n):
                # If neighbor is directly connected and not yet visited
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        # Go through each city
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)  # Visit all cities in the current province
                provinces += 1  # After one DFS, one full province is found

        return provinces

        # ✅ Time Complexity: O(n^2)
        # - Outer loop runs n times
        # - Each DFS checks up to n neighbors
        # - Total: O(n * n)

        # ✅ Space Complexity: O(n)
        # - visited[] list of size n
        # - DFS recursion stack can go as deep as n in the worst case...
