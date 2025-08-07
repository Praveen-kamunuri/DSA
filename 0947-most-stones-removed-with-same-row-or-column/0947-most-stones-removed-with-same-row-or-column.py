class Solution:

    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]


    def union(self, parent, rank, u, v):
        pu = self.find(parent, u)
        pv = self.find(parent, v)

        if pu == pv:
            return

        if rank[pu] < rank[pv]:
            parent[pu] = pv

        elif rank[pu] > rank[pv]:
            parent[pv] = pu
        
        else:
            parent[pv] = pu
            rank[pu] += 1

    def removeStones(self, stones: List[List[int]]) -> int:

        def add(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0

        parent = {}
        rank = {}

        max_row = 0
        for row, col in stones:
            max_row = max(max_row, row)
        
        offset = max_row + 1

        for x, y in stones:
            row = x
            col = y + offset
            add(row)
            add(col)
            self.union(parent, rank, row, col)
        
        components = set(self.find(parent, node) for node in parent)

        return len(stones) - len(components)
        