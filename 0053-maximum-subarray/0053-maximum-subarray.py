class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        maxi = nums[0]
        for i in range(n):
            summ += nums[i]
            if summ > maxi:
                maxi = summ
            if summ < 0:
                summ = 0
        return maxi
        