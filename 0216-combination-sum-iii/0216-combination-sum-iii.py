class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        ds = []
        
        def findComb(num, summ, size):
            if size == k:
                if summ == n:
                    res.append(ds[:])
                return
            
            if num > 9:
                return
            
            ds.append(num)
            findComb(num + 1, summ + num, size + 1)
            ds.pop()
            findComb(num + 1, summ, size)
            
        findComb(1 , 0 , 0)
        return res