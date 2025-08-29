# From Intuition:
# The goal is to reach the bottom-right cell (n-1, n-1) in the minimum "time" t, 
# where "time" is defined as the max height encountered along the path.
# You can only step into a cell if its value is <= t.
# So, we want the path from (0,0) to (n-1,n-1) with the minimum maximum height.
#
# This is a classic case for **Dijkstra's Algorithm**:
# - Each cell is a node
# - The cost of entering a node is its height (grid value)
# - We're minimizing the "max height" encountered, not the sum of weights
# - Use a min-heap (priority queue) to always expand the lowest available "height" cell

import heapq
class Solution:

    def isValid(self, row, col, n):
        # Helper to check bounds
        return 0 <= row < n and 0 <= col < n

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Track visited cells
        visited = [[0 for _ in range(n)] for _ in range(n)]

        # Min-heap (priority queue): (time, (row, col))
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], (0, 0)))

        # Mark starting cell as visited
        visited[0][0] = 1

        # Track max height seen so far on the path
        maxi = 0

        while min_heap:
            # Get cell with lowest water level seen so far
            time, (row, col) = heapq.heappop(min_heap)

            # Update max height seen
            maxi = max(maxi, time)

            # If we reached bottom-right cell, return the answer
            if row == n - 1 and col == n - 1:
                return maxi

            # Move in 4 directions
            drow = [-1, 1, 0, 0]
            dcol = [0, 0, -1, 1]

            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                # Check if neighbor is valid and not visited
                if self.isValid(nrow, ncol, n) and visited[nrow][ncol] == 0:
                    nodeNo = grid[nrow][ncol]

                    # Add to heap and mark as visited
                    heapq.heappush(min_heap, (nodeNo, (nrow, ncol)))
                    visited[nrow][ncol] = 1

# -------------------------------------------------------------
# Time Complexity: O(n^2 * log(n^2))
# - Each of the n^2 cells can be pushed to the heap at most once.
# - Heap operations take log(n^2) time.

# Space Complexity: O(n^2)
# - Visited matrix: O(n^2)
# - Heap can grow up to O(n^2) elements in the worst case.

# This approach is optimal for this problem and mirrors Dijkstra’s algorithm,
# adapted to minimize the max weight (height) on a path rather than the sum.
