class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solve(ind, ans, ds):
            if ind == n:
                ans.append(ds[:])
                return
                
            ds.append(nums[ind])
            solve(ind + 1, ans, ds)
            ds.pop()
            solve(ind + 1, ans, ds)
            
            
        
        
        n = len(nums)
        ans = []
        ds = []
        
        
        solve(0, ans, ds)
        return ans