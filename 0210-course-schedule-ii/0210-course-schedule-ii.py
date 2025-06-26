class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def is_cycle(node, adj, visited, path_sum, n, result):

            visited[node] = 1
            path_sum[node] = 1

            for neighbour in adj[node]:
                if visited[neighbour] != 1:
                    if is_cycle(neighbour, adj, visited, path_sum, n, result) == False:
                        return False
                elif path_sum[neighbour] == 1:
                    return False
            path_sum[node] = 0
            result.append(node)
            return True

        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)
        
        visited = [0] * numCourses
        path_sum = [0] * numCourses
        result = []

        for i in range(numCourses):
            if visited[i] != 1:
                if is_cycle(i, adj, visited, path_sum, numCourses, result) == False:
                    return []
        return result[::-1]