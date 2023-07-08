class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        cur_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_count += 1
            else:
                max_count = max(max_count, cur_count)
                cur_count = 0
        max_count = max(max_count, cur_count)  # Update max_count after the loop ends
        return max_count
