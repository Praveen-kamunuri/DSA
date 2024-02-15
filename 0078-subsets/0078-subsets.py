class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        def generate(n, ds, ans, ind):
            if ind == n:
                ans.append(ds[:])
                return
            
          
            ds.append(nums[ind])
            generate(n, ds, ans, ind + 1)
            ds.pop()
            generate(n, ds, ans, ind + 1)
        
        
        n = len(nums)
        ds = []
        ans = []
        
        
        generate(n, ds, ans, 0)
        return ans