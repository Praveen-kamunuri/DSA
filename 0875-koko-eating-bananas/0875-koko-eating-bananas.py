import  math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def find_max(piles):
            n = len(piles)
            maxi = piles[0]
            for i in range(n):
                if piles[i] > maxi:
                    maxi = piles[i]
            return maxi
        
        
        
        def calTotalH(piles, Hourly):
            n = len(piles)
            total_h = 0
            for i in range(n):
                total_h += math.ceil(piles[i] / Hourly)
            return total_h
                
                
        
        
        low = 1
        
        high = find_max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            
            totalH = calTotalH(piles, mid)
            
            if totalH <= h:
                high = mid - 1
            
            else:
                low  = mid + 1
        return low
        
        
        