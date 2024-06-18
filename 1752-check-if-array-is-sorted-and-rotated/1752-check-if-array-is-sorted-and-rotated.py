class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        peek = 0
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                peek += 1
                
        
        if nums[n-1] > nums[0]:
            peek += 1
            
        if peek <= 1:
            return True
        else:
            return False
        
        