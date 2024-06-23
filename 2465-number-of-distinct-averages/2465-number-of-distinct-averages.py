class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        res = set()
        
        nums.sort()
        
        
        while nums:
            n =  len(nums)
            
            mini = nums[0]
            maxi = nums[n-1]
            
            res.add((mini + maxi) / 2)
            
            nums[:] = nums[1:n-1]
            
        return len(res)