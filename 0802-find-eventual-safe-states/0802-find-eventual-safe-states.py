from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        # Step 1: Create the reversed graph
        rev_adj = [[] for _ in range(V)]  # reversed adjacency list
        indegree = [0] * V                # indegree array for the original graph

        # Step 2: Reverse the edges and calculate indegree
        for u in range(V):
            for v in graph[u]:
                rev_adj[v].append(u)      # reverse the edge u -> v to v -> u
                indegree[u] += 1          # count how many outgoing edges node u has

        # Step 3: Add all terminal (safe) nodes (with 0 outgoing edges) to queue
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        # Step 4: Topological sort using BFS on reversed graph
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)  # this node is safe

            for neighbour in rev_adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        topo.sort()  # sort the result as per problem requirement
        return topo

# Time Complexity: O(V + E)
# - Reversing the graph: O(E)
# - Initial indegree computation: O(E)
# - BFS traversal over all nodes and edges: O(V + E)
# - Sorting result: O(V log V)

# Space Complexity: O(V + E)
# - rev_adj takes O(V + E)
# - indegree and queue take O(V)
# - topo list takes O(V)


