class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        for j in range(1,n):
            if nums[i] == nums[j]:
                continue
            else:
                nums[i+1] = nums[j]
                
                i = i + 1
                
        return i + 1
            
                
                
                