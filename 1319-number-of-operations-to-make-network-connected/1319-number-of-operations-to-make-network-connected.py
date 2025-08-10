from typing import List

class Solution:
    # ✅ ALGORITHM USED: Disjoint Set Union (DSU) / Union-Find
    # ➤ Optimized with Path Compression & Union by Rank
    # ➤ Purpose: Efficiently manage connected components in an undirected graph
    
    # FIND with path compression
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])  # compress path
        return parent[node]

    # UNION with rank
    def union(self, parent, rank, u, v):
        pu = self.find(parent, u)
        pv = self.find(parent, v)

        if pu == pv:
            return  # already connected, no union needed

        # Union by rank (attach smaller tree under larger)
        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pu] > rank[pv]:
            parent[pv] = pu
        else:
            parent[pv] = pu
            rank[pu] += 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        \U0001f9e0 INTUITION:
        - To connect `n` computers into a single network, you need at least (n - 1) cables.
        - If we have fewer than (n - 1) connections, it's impossible → return -1.
        - Use DSU to group computers into connected components.
        - Count how many redundant (extra) connections exist.
        - To connect `k` components, we need exactly `k - 1` edges.
        - If we have enough extra edges (≥ k - 1), we can connect the whole network.
        """

        # Step 1: Check if we even have enough connections
        if len(connections) < n - 1:
            return -1  # Not enough edges

        # Step 2: Initialize DSU parent and rank arrays
        parent = [i for i in range(n)]
        rank = [0] * n
        extra_edges = 0  # tracks redundant connections

        # Step 3: Process each connection
        for u, v in connections:
            pu = self.find(parent, u)
            pv = self.find(parent, v)

            if pu == pv:
                # Already connected → this is an extra edge
                extra_edges += 1
            else:
                # Connect the two components
                self.union(parent, rank, pu, pv)

        # Step 4: Count number of connected components
        components = len(set(self.find(parent, i) for i in range(n)))

        # Step 5: If we have enough extra edges to connect all components, return answer
        required = components - 1
        if extra_edges >= required:
            return required
        else:
            return -1


# ------------------------------------------------------------------------------
# ✅ Time Complexity:
# - DSU operations (find/union) are nearly constant time: O(α(N)) ≈ O(1)
# - Processing connections: O(E * α(N)) where E = number of connections
# - Counting components: O(N * α(N))
# - Total: O(N + E)

# ✅ Space Complexity:
# - O(N) for parent array
# - O(N) for rank array
# ------------------------------------------------------------------------------
