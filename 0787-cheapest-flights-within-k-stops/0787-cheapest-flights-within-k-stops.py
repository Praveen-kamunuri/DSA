import sys
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[]for _ in range(n)]
        for u, v, wt in flights:
            adj[u].append((v, wt))
        distance = [sys.maxsize] * n
        q = deque()
        distance[src] = 0
        q.append((0, (src, 0)))

        while q:
            stops, node_with_cost = q.popleft()
            node = node_with_cost[0]
            cost = node_with_cost[1]

            if stops > k:
                continue
            else:
                for neighbour, wt in adj[node]:
                    if cost + wt < distance[neighbour] and stops <= k:
                        distance[neighbour] = cost + wt
                        q.append((stops + 1, (neighbour, cost + wt)))
        if distance[dst] == sys.maxsize:
            return -1
        else:
            return distance[dst]

        