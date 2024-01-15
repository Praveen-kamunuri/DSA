class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ds = []
        res = []
        
        def generate(ind):
            if ind == len(s):
                res.append(ds[:])
                return
            
            for i in range(ind , len(s)):
            
                if isPal(s,ind,i):
                    ds.append(s[ind:i+1])
                    generate(i + 1)
                    ds.pop()
                
            
        def isPal(s,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True
                    
        
        
        generate(0)
        return res