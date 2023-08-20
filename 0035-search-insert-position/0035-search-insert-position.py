class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n  # Initialize ans with a default value (last index + 1)
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] >= target:
                ans = mid  # Update ans with the current mid index
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
