class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, adj, tin, low, vis, bridges):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1

        for adj_node in adj[node]:
            if adj_node == parent:
                continue
            
            if vis[adj_node] == 0:
                self.dfs(adj_node, node, adj, tin, low, vis, bridges)
                low[node] = min(low[node], low[adj_node])
                if low[adj_node] > tin[node]:
                    bridges.append([node, adj_node]) 
            
            else:
                low[node] = min(low[node], low[adj_node])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj = [[]for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n
        
        tin = [0] * n
        low = [0] * n

        bridges = []

        self.dfs(0, -1, adj, tin, low, visited, bridges)

        return bridges



        