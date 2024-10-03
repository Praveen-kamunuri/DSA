class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def solve(nums, k):
            if k < 0:
                return 0
            
            n = len(nums)
            l = 0
            summ = 0
            cnt = 0
            
            for r in range(n):
                summ += nums[r] % 2
                
                while summ > k:
                    summ -= nums[l] % 2
                    l += 1
                
                cnt += r - l + 1
            return cnt
        
        
        
        return solve(nums, k) - solve(nums, k - 1)
        