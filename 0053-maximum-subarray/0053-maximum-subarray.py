class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        maxi = nums[0]
        
        n = len(nums)
        
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum > maxi:
                maxi = curr_sum
                
            if curr_sum < 0:
                curr_sum = 0
        return maxi
        