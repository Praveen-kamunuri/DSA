class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = 0
        maxi = nums[0]
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > maxi:
                maxi =  cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return maxi