class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def generate(n, ds, ans, target, ind, summ):
            if ind == n:
                if summ == target:
                    ans.append(ds[:])
                return
            
            if summ + candidates[ind] <= target:
                ds.append(candidates[ind])
                generate(n, ds, ans, target, ind, summ + candidates[ind])
                ds.pop()
                
            
            generate(n, ds, ans, target, ind + 1, summ)
    
        n = len(candidates)
        ds = []
        ans = []
        
        generate(n, ds, ans, target, 0, 0)
        return ans