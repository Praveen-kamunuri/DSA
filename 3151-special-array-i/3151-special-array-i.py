class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        def findParity(a, b):
            if (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):
                return True
            else:
                return False
        
        
        n = len(nums)
        
        for i in range(n-1):
            if findParity(nums[i], nums[i+1]):
                continue
            else:
                return False
            
        return True
                
            
        