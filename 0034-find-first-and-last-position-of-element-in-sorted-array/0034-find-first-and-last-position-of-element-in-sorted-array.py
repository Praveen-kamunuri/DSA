class Solution:
    def lowerBound(self,nums,target):
        n = len(nums)
        low = 0
        high = n - 1
        low_bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                low_bound = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low_bound
    
    def upperBound(self,nums,target):
        n = len(nums)
        low = 0
        high = n -1
        up_bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                up_bound = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return up_bound
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.lowerBound(nums,target)
        second = self.upperBound(nums,target)
        return [first,second]
            
        
        