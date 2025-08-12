import sys
import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        # Initialize the distance (effort) matrix with infinity
        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]

        # Min-heap priority queue: (effort, (row, col))
        min_heap = []
        heapq.heappush(min_heap, (0, (0, 0)))
        distance[0][0] = 0  # Starting point has 0 effort

        # 4-directional movement: up, down, left, right
        del_row = [-1, 1, 0, 0]
        del_col = [0, 0, -1, 1]

        # Dijkstra's algorithm is used here to find the minimum effort path
        while min_heap:
            diff, (row, col) = heapq.heappop(min_heap)

            # If destination is reached, return the current minimum effort
            if row == rows - 1 and col == cols - 1:
                return diff

            # Explore all 4 neighbors
            for i in range(4):
                new_row = row + del_row[i]
                new_col = col + del_col[i]

                # Check for valid grid boundaries
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate the effort to move to the neighboring cell
                    current_effort = abs(heights[row][col] - heights[new_row][new_col])
                    new_effort = max(diff, current_effort)  # take the max effort along the path

                    # Update if a less effortful path is found
                    if new_effort < distance[new_row][new_col]:
                        distance[new_row][new_col] = new_effort
                        heapq.heappush(min_heap, (new_effort, (new_row, new_col)))

        # Should never reach here in a valid input grid
        return 0

"""
\U0001f4cc Algorithm Used: Dijkstra's Algorithm (modified)
--------------------------------------------------
- This problem is a variation of the shortest path problem.
- Instead of minimizing the sum of weights (as in classical Dijkstra),
  here we minimize the **maximum edge weight (effort)** along the path.
- We use a priority queue (min-heap) to always expand the cell with the least current effort.
- The 'distance' matrix keeps track of the minimum effort to reach each cell.

\U0001f9ee Time Complexity (TC): O(N * M * log(N * M))
- Each of the N*M cells can be inserted into the heap at most once.
- Heap operations (`heappush` and `heappop`) take O(log N*M) time.

\U0001f4be Space Complexity (SC): O(N * M)
- For the distance matrix and the heap (in worst case).

✅ Why this works:
- The effort is defined as the **maximum absolute height difference** between adjacent cells along a path.
- Dijkstra's algorithm, modified to use max instead of sum, guarantees the minimum such value.
"""
