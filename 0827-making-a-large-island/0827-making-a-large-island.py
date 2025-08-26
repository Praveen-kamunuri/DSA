# Intuition:
# ------------
# We are given a grid of 0s (water) and 1s (land).
# We want to find the size of the largest island we can form 
# if we can change at most one 0 into a 1.
#
# Observations:
# - An island is just a connected component of 1s (connected 4-directionally).
# - We can think of each cell as a node in a graph.
# - Two nodes (cells) are connected if they are both 1 and adjacent.
# - To efficiently merge and query component sizes, we can use Disjoint Set Union (DSU).
#
# Approach:
# 1. First, connect all the 1s using DSU (union by size).
# 2. Then, for each 0-cell, check its 4 neighbors:
#    - Collect unique neighboring components (using DSU find).
#    - If we flip this 0 to 1, the new island size = sum of neighboring components + 1.
# 3. Keep track of the maximum island size possible.
# 4. Edge case: If the grid is all 1s already, the answer is the largest DSU component.

from typing import List

# ----------------- Disjoint Set Union (Union Find) ----------------- #
class DSU:
    def __init__(self, n):
        # rank is used in union by rank (not necessary for size-based unions but kept for completeness)
        self.rank = [0] * (n + 1)
        # parent[i] = parent of node i
        self.parent = [i for i in range(n + 1)]
        # size[i] = size of component whose leader is i
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        # Path compression for efficiency
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        # Union two sets by rank
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return 
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        # Union two sets by size
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


# ----------------- Main Solution ----------------- #
class Solution:

    def isValid(self, row, col, n):
        # Check if (row, col) lies inside the grid boundaries
        return 0 <= row < n and 0 <= col < n

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        ds = DSU(n * n)  # DSU with n*n nodes (each cell = node)

        # Step 1: Connect existing land cells (1s) in DSU
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                drow = [-1, 1, 0, 0]
                dcol = [0, 0, -1, 1]

                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]

                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        nodeNo = (row * n) + col
                        adjNodeNo = (nrow * n) + ncol
                        ds.unionBySize(nodeNo, adjNodeNo)

        maxi = 0

        # Step 2: Try flipping each 0 → 1 and calculate island size
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                
                drow = [-1, 1, 0, 0]
                dcol = [0, 0, -1, 1]

                components = set()  # store unique neighboring components

                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]

                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        components.add(ds.findUPar((nrow * n) + ncol))
                
                subTotal = 0
                for comp in components:
                    subTotal += ds.size[comp]
                
                maxi = max(maxi, subTotal + 1)  # +1 for the flipped cell

        # Step 3: Edge case – if all are 1s already
        for cellNo in range(n * n):
            maxi = max(maxi, ds.size[ds.findUPar(cellNo)])

        return maxi


# ----------------- Complexity Analysis ----------------- #
# Time Complexity: 
# - Building DSU (connecting neighbors): O(n^2 * 4 * α(n^2)) ≈ O(n^2)
#   where α is inverse Ackermann (almost constant).
# - Checking each 0 cell and its neighbors: O(n^2 * 4) = O(n^2)
# - Overall: O(n^2)
#
# Space Complexity:
# - DSU arrays (parent, size, rank): O(n^2)
# - Grid storage: O(n^2)
# - Components set at most size 4 → O(1)
# - Overall: O(n^2)
