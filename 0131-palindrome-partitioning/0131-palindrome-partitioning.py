class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        
        
        def generate(ind):
            if ind == len(s):
                res.append(path[:])
                return
            
            for i in range(ind , len(s)):
                if ispal(s , ind, i):
                    path.append(s[ind:i+1])
                    
                    generate(i + 1)
                    path.pop()
                
        
        def ispal(s, start, end):
            
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            
            return True
                
        generate(0)
        return res
    
        
        