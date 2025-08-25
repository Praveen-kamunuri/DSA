class DSU:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return 
        
        elif self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        
class Solution:

    def isValid(self, row, col, n):
        if row >= 0 and row < n and col >= 0 and col < n:
            return True
        else:
            return False


    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid[0])

        ds = DSU(n * n)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                drow = [-1, 1, 0 , 0]
                dcol = [0, 0, -1, 1]

                for i in range(4):
                    nrow = drow[i] + row
                    ncol = dcol[i] + col

                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        nodeNo = (row * n) + col
                        adjNodeNo = (nrow * n) + ncol
                        ds.unionBySize(nodeNo, adjNodeNo)

        maxi = 0
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                
                drow = [-1, 1, 0, 0]
                dcol = [0, 0, -1, 1]

                components = set()

                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]

                    if self.isValid(nrow, ncol, n) and grid[nrow][ncol] == 1:
                        components.add(ds.findUPar((nrow * n) + ncol))
                
                subTotal = 0
                for comp in components:
                    subTotal += ds.size[comp]
                
                maxi = max(maxi, subTotal + 1)
        
        for cellNo in range(n * n):
            maxi = max(maxi, ds.size[ds.findUPar(cellNo)])
        return maxi
