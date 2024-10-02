class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def solve(nums, k):
            if k < 0:
                return 0
                
            n = len(nums)
            l = 0
            summ = 0
            cnt = 0

            for r in range(n):
                summ += nums[r]

                while summ > k:
                    summ -= nums[l]
                    l += 1
                cnt += r - l + 1
            return cnt

        return solve(nums, goal) - solve(nums, goal - 1)
        
                
            