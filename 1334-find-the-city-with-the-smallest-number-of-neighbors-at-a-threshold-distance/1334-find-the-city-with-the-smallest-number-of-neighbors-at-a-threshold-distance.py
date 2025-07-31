import sys
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        matrix = [[sys.maxsize for _ in range(n)]for _ in range(n)]

        for u, v, wt in edges:
            matrix[u][v] = wt
            matrix[v][u] = wt

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        cities = [0] * n

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and matrix[i][j] <= distanceThreshold:
                    cnt += 1
            cities[i] = cnt
        city = -1
        city_count = sys.maxsize

        for i in range(n):
            if cities[i] < city_count:
                city_count = cities[i]
                city = i
            elif cities[i] == city_count:
                city = max(city, i)
        return city

