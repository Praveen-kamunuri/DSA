import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def max_h(piles):
            maxi = piles[0]
            for i in range(len(piles)):
                if piles[i] > maxi:
                    maxi = piles[i]
            return maxi
        
        
        def calTotal_h(piles, hours):
            total = 0
            
            n = len(piles)
            for i in range(n):
                total += math.ceil(piles[i] / hours)
            return total
        
        low = 1
        high = max_h(piles)
        
        while low <= high:
            mid = (low + high) // 2
            total_h = calTotal_h(piles, mid)
            
            if total_h <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low