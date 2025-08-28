class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, visited, adj, tin, low, bridges):
        visited[node] = 1
        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1
        for neighbour in adj[node]:
            if neighbour == parent:
                continue
                
            if visited[neighbour] == 0:
                self.dfs(neighbour, node, visited, adj, tin, low, bridges)
                low[node] = min(low[node], low[neighbour])
                if low[neighbour] > tin[node]:
                    bridges.append((neighbour, node))
            else:
                low[node] = min(low[node], low[neighbour])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:


        adj = [[]for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []
        self.dfs(0, -1, visited, adj, tin, low, bridges)
        return bridges



        
        