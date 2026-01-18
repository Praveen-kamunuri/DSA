import sys
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)

        prev = [0] * len(triangle[-1])

        prev[0] = triangle[0][0]

        for i in range(1, rows):
            cols = i + 1
            temp = [0] * cols
            for j in range(cols):
                if j == 0:
                    temp[j] += triangle[i][j] + prev[j]
                elif j == i:
                    temp[j] += triangle[i][j] + prev[j - 1]
                else:
                    temp[j] += triangle[i][j] +  min(prev[j], prev[j - 1])
            prev = temp

        res = sys.maxsize
        for k in range(len(prev)):
            if prev[k] < res:
                res = prev[k]
        return res




        