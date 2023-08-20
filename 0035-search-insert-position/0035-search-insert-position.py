class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        low_bound = n 
        while low <= high:
            mid = (low + high) //2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] >= target:
                low_bound = mid
                high = mid - 1
        return low_bound