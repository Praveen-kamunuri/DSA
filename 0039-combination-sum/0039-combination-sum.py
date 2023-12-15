class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        
        def findCombinations(ind , target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return 
            
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombinations(ind , (target - candidates[ind]) )
                ds.pop()
                
            findCombinations(ind + 1 , target)
                
        findCombinations(0 , target)
        return ans
                
                
        
        
        
        
        
        
        
        
        findCombinations(0 , target)
        
        
        