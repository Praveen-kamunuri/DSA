class Solution:
    def climbStairs(self, n: int) -> int:

        def backtrack(summ, ds, res, n):
            if summ > n:
                return 
            
            elif summ == n:
                res.append(ds[:])
                return
            
            else:
                backtrack(summ + 2, ds, res, n)
                backtrack(summ + 1, ds, res, n)
            
            
        res = []
        ds = []
        backtrack(0, ds, res, n)
        return len(res)