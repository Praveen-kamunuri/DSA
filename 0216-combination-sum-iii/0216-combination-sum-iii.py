class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ds = []
        ans = []
        def generate(num, summ, size):
            if size == k:
                if summ == n:
                    ans.append(ds[:])
                return
            
            if num > 9:
                return
            
            ds.append(num)
            
            generate(num + 1, summ + num , size + 1)
            
            ds.pop()
            
            generate(num + 1, summ, size)
            
    
        generate(1,0,0)
        
        return ans
        