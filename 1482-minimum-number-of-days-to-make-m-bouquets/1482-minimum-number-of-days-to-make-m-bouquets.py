class Solution(object):
    def is_poss(self, bloomDay, Day, boque, req_flowers):
        n = len(bloomDay)
        cnt = 0
        possible = 0
        for i in range(n):
            if bloomDay[i] <= Day:
                cnt += 1  # Count the flowers that have bloomed until the given day
            else:
                possible += (cnt // req_flowers)  # Calculate possible bouquets and add to total
                cnt = 0  # Reset count for the next potential bouquet
        possible += (cnt // req_flowers)  # Calculate possible bouquets for remaining flowers
        return possible  # Return the total possible bouquets
        
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1  # Not enough flowers to make required bouquets
        
        low = min(bloomDay)  # Minimum bloom day
        high = max(bloomDay)  # Maximum bloom day
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2  # Middle of the search range
            poss = self.is_poss(bloomDay, mid, m, k)  # Calculate possible bouquets
            
            if poss >= m:  # If enough bouquets are possible
                ans = mid  # Update answer
                high = mid - 1  # Search for smaller days
            else:
                low = mid + 1  # Search for larger days
        
        return ans  # Return the minimum number of days required to make the required bouquets
