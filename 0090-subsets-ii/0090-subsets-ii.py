class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ds = []
        ans = []
        
        
        def generate(ind):
            ans.append(ds[:])
            
            for i in range(ind , n):
                if i != ind and nums[i] == nums[i-1]:
                    continue
                    
                ds.append(nums[i])
                
                generate(i + 1)
                ds.pop()
                
        
        nums.sort()
        generate(0)
        return ans