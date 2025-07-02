from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        V = len(graph)

        rev_adj = [[]for _ in range(V)]

        indegree = [0] * V




        for u in range(V):
            for v in graph[u]:
                rev_adj[v].append(u)
                indegree[u] += 1

        q = deque()
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            for neighbour in rev_adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
            topo.append(node)

        topo.sort()
        return topo  

        



        