class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        l_sum = 0
        
        r_sum = 0
        
        max_sum = 0
        
        for i in range(k):
            l_sum += cardPoints[i]
            
            max_sum = l_sum
        
        right_ind = n - 1
        
        for j in range(k-1, -1, -1):
            
            l_sum = l_sum - cardPoints[j]
            
            r_sum = r_sum + cardPoints[right_ind]
            
            max_sum = max(max_sum, l_sum + r_sum)
            
            right_ind -= 1
        return max_sum
            
        
        
        
        
        