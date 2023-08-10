class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        left = 0
        maxFreq = 0
        operations = 0

        for right in range(len(nums)):
            operations += (nums[right] - nums[right - 1]) * (right - left)

            while operations > k:
                operations -= nums[right] - nums[left]
                left += 1

            maxFreq = max(maxFreq, right - left + 1)

        return maxFreq

        