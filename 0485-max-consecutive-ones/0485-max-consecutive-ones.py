class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_c = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                max_c = max(max_c,cur)
                cur = 0
        return max(max_c,cur)