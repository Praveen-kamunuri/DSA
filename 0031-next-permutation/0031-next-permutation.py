class Solution(object):
    def nextPermutation(self, nums):
        # Find the first index from the right where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
    
        if i >= 0:
            # Find the first index from the right where nums[j] > nums[i]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
    
        # Reverse the suffix starting from i+1
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    