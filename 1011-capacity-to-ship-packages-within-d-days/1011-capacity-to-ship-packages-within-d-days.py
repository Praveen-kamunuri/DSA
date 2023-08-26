class Solution(object):
    def find_days(self,weights,cap):
        n = len(weights)
        days = 1
        load = 0
        for i in range(n):
            if weights[i] + load > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days
            
        
    
    
    
    
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            days_req = self.find_days(weights,mid)
            if days_req <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            