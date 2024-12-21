class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        left = [0] * n
        
    
        
        left[0] = 1
        
           
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
                
        curr = 1
        right = 1
        summ = max(1, left[n - 1])
        
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                curr = right + 1
                right = curr
                
                
            else:
                curr = 1
                right = 1
            
            summ = summ + max(left[j], curr)
                
                
        return summ
        
      