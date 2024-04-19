class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def solve(ind, n, ds, ans):
            if ind == n:
                ans.append(ds[:])
                return
            
            ds.append(nums[ind])
            solve(ind + 1, n, ds, ans)
            ds.pop()
            solve(ind + 1, n, ds, ans)
            
        
        n = len(nums)
        ds = []
        ans = []
        solve(0, n, ds, ans)
        return ans