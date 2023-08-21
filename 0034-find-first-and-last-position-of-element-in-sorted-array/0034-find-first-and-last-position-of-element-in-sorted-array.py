class Solution(object):
    def start_ind(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def end_ind(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        end = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                end = mid
                low  = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return end
                
                
    def searchRange(self, nums, target):
        start = self.start_ind(nums,target)
        end = self.end_ind(nums,target)
        return [start,end]
       