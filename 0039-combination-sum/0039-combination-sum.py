class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def generate(n, ds, res, target, ind, summ):
            
            if ind == n:
                if summ == target:
                    res.append(ds[:])
                return
            
            if candidates[ind] + summ <= target:
                
                ds.append(candidates[ind])
            
                generate(n, ds, res,  target, ind, summ + candidates[ind])
                ds.pop()
                
            
            generate(n, ds, res, target, ind+1 , summ)
        
        
        
        
        ds = []
        
        res = []
        
        n = len(candidates)
        
        generate(n, ds, res, target, 0, 0)
        
        return res
        