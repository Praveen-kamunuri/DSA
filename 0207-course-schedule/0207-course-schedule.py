class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def is_cycle(node, adj, visited, path_sum):
            visited[node] = 1
            path_sum[node] = 1

            for neighbour in adj[node]:
                if visited[neighbour] == 0:
                    if is_cycle(neighbour, adj, visited, path_sum) == True:
                        return True
                elif path_sum[neighbour] == 1:
                    return True
            path_sum[node] = 0
            return False

        adj = [[]for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)

        visited = [0] * numCourses
        path_sum = [0] * numCourses

        for i in range(numCourses):
            if visited[i] == 0:
                if is_cycle(i, adj, visited, path_sum) == True:
                    return False
            
        return True