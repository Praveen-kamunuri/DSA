class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        
        n = len(nums)
        
        nge = [-1] * n
        
        for i in range(n):
            
            for j in range(i+1, i + n):
                
                ind = j % n
                
                if nums[ind] > nums[i]:
                    nge[i] = nums[ind]
                    break
        return nge
                
                
        