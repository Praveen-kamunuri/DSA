class Solution(object):
    def isPossible(self,bloomDay,Day,boquet,flowers):
        n = len(bloomDay)
        cnt = 0
        No_of_boquet = 0
        for i in range(n):
            if bloomDay[i] <= Day:
                cnt += 1
            else:
                No_of_boquet += ( cnt // flowers)
                cnt = 0
        No_of_boquet += (cnt//flowers)
        return No_of_boquet 
    
    
    
    
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            poss = self.isPossible(bloomDay,mid,m,k)
            if poss >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
            
                
            
            