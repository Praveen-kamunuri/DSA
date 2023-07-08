class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n + 1):  # Include the last number in the range
            if i not in nums:
                return i
