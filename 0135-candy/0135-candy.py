class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        left = [0] * n
        
        right = [0] * n
        
        left[0] = 1
        
        right[n-1] = 1
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right[j] = right[j + 1] + 1
            else:
                right[j] = 1
        
        total_chocolates = 0
        for k in range(n):
            total_chocolates += max(left[k], right[k])
        return total_chocolates
            
            