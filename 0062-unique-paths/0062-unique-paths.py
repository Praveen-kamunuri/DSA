class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prev = [0] * n

        prev[0] = 1

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                
                if i == 0 and j == 0:
                    temp[j] = 1
                else:
                    temp[j] = prev[j] + temp[j - 1]
            prev = temp
        return temp[n - 1]