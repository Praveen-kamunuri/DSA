import sys
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize adjacency matrix with "infinity"
        matrix = [[sys.maxsize for _ in range(n)] for _ in range(n)]

        # Step 2: Set distances from each city to itself as 0
        for i in range(n):
            matrix[i][i] = 0

        # Step 3: Populate initial edge weights (bidirectional)
        for u, v, wt in edges:
            matrix[u][v] = wt
            matrix[v][u] = wt

        # Step 4: Floyd-Warshall to compute all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != sys.maxsize and matrix[k][j] != sys.maxsize:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # Step 5: Count reachable cities within the threshold for each city
        city_count = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and matrix[i][j] <= distanceThreshold:
                    cnt += 1
            city_count[i] = cnt

        # Step 6: Find the city with the smallest count of reachable cities
        # If tie, prefer the city with the greater index
        min_city = -1
        min_count = sys.maxsize

        for i, val in enumerate(city_count):
            if val < min_count:
                min_count = val
                min_city = i
            elif val == min_count:
                if i > min_city:
                    min_city = i

        return min_city


# \U0001f9e0 Time Complexity (TFC):
# - Floyd-Warshall: O(n^3)
# - Counting neighbors: O(n^2)
# - Final comparison: O(n)
# => Total: **O(n^3)**

# \U0001f4e6 Space Complexity (SC):
# - Distance matrix: O(n^2)
# - Count list: O(n)
# => Total: **O(n^2)**
