class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, col):
            color[node] = col
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if not dfs(neighbour, 1 - col):
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True

        n = len(graph)

        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True