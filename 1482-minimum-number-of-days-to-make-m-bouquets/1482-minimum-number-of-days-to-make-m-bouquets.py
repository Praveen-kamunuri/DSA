class Solution(object):
    def is_poss(self,bloomDay,Day,boque,req_flowers):
        n = len(bloomDay)
        cnt = 0
        possible = 0
        for i in range(n):
            if bloomDay[i] <= Day:
                cnt += 1
            else:
                possible += (cnt//req_flowers)
                cnt = 0
        possible += (cnt//req_flowers)
        return possible
                
    
    
    
    
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            poss = self.is_poss(bloomDay,mid,m,k)
            if poss >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
                
        