class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1 and nums[0] == 0:
                return
        
        
        
        j = -1
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
                
        for i in range(j+1,n):
            if nums[i] != 0:
                nums[j] , nums[i] = nums[i] , nums[j]
                j += 1
        
        
        