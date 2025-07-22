import sys
import heapq 
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj = [[]for _ in range(n)]
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        distance = [sys.maxsize] * n
        ways = [0] * n

        distance[0] = 0
        ways[0] = 1

        mod_val = (10 ** 9) + 7

        min_heap = []

        heapq.heappush(min_heap, (0, 0))

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            for neighbour, edge_wt in adj[node]:
                if dist + edge_wt < distance[neighbour]:
                    distance[neighbour] = dist + edge_wt
                    ways[neighbour] = ways[node]
                    heapq.heappush(min_heap, (dist + edge_wt, neighbour))
                elif dist + edge_wt == distance[neighbour]:
                    ways[neighbour] = (ways[neighbour] + ways[node]) % mod_val
        print(distance)
        return ways[n - 1 ] % mod_val





        




        