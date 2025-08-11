from typing import List

class Solution:

    # -----------------------------------
    # Union-Find (Disjoint Set Union) class methods
    # -----------------------------------

    # Path compression in find to optimize the tree height..
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    # Union by rank to keep tree flat
    def union(self, parent, rank, u, v):
        pu = self.find(parent, u)
        pv = self.find(parent, v)

        if pu == pv:
            return  # already in the same component

        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pu] > rank[pv]:
            parent[pv] = pu
        else:
            parent[pv] = pu
            rank[pu] += 1

    # -----------------------------------
    # Main function to solve the problem
    # -----------------------------------

    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Intuition:
        - Each stone can be removed if there is another stone in the same row or column.
        - We can think of this as a graph problem, where stones are nodes connected by rows and columns.
        - If multiple stones are connected by rows or columns, they form a connected component.
        - In each connected component, we can remove all stones except one.
        - So, max stones removed = total stones - number of connected components

        Approach:
        - Use Union-Find to group stones by row and column.
        - Since rows and columns can have the same value (e.g., row 0 and column 0), we offset the column index.
        - Each unique row or col becomes a node in the union-find.
        """

        def add(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0

        parent = {}
        rank = {}

        # Determine offset to separate row and col indices
        max_row = 0
        for row, col in stones:
            max_row = max(max_row, row)
        offset = max_row + 1  # ensure no overlap between rows and cols

        # Union row and column for each stone
        for x, y in stones:
            row = x
            col = y + offset  # offset col to avoid clash with row index
            add(row)
            add(col)
            self.union(parent, rank, row, col)

        # Count number of unique components (ultimate parents)
        components = set(self.find(parent, node) for node in parent)

        # Answer = total stones - number of connected components
        return len(stones) - len(components)


# -----------------------------------
# Time and Space Complexity Analysis
# -----------------------------------
# Let n be the number of stones.

# Time Complexity:
# - For each stone: O(α(n)) for union and find operations (inverse Ackermann function, almost constant)
# - Overall: O(n * α(n)) ~ O(n)

# Space Complexity:
# - parent and rank dictionaries: O(n) in worst case
# - Total: O(n)
