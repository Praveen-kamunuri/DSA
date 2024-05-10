import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Function to find the maximum pile size
        def find_max(piles: List[int]) -> int:
            n = len(piles)
            maxi = piles[0]
            for i in range(n):
                if piles[i] > maxi:
                    maxi = piles[i]
            return maxi
        
        # Function to calculate total hours required to eat all piles at given speed
        def calTotalH(piles: List[int], Hourly: int) -> int:
            n = len(piles)
            total_h = 0
            for i in range(n):
                total_h += math.ceil(piles[i] / Hourly)
            return total_h
                
        # Initialize low and high for binary search
        low = 1
        high = find_max(piles)
        
        # Binary search for the minimum eating speed
        while low <= high:
            mid = (low + high) // 2
            
            totalH = calTotalH(piles, mid)
            
            if totalH <= h:
                high = mid - 1
            else:
                low  = mid + 1
                
        # Return the minimum eating speed
        return low
