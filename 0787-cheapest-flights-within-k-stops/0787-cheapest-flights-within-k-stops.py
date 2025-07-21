import sys
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[]for _ in range(n)]

        for u, v, wt in flights:
            adj[u].append((v, wt))

        q = deque()

        distance = [sys.maxsize] * n

        q.append((0, (src, 0)))

        distance[src] = 0

        while q:
            stops, node_with_delay = q.popleft()
            node = node_with_delay[0]
            delay = node_with_delay[1]

            if stops > k:
                continue
            
            for neighbour, edge_wt in adj[node]:
                 if delay + edge_wt < distance[neighbour] and stops <= k:
                    distance[neighbour] =  delay + edge_wt
                    q.append((stops + 1, (neighbour, delay + edge_wt)))

        print(distance)

        if distance[dst] == sys.maxsize:
            return -1
        else:
            return distance[dst]
        


        


        