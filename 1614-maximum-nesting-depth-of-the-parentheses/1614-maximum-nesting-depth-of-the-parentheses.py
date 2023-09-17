class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "":
            return 0
        
        
        
        
        curr_max = 0
        maxi = 0
        for i in s:
            if i == "(":
                curr_max += 1
            elif i == ")":
                maxi = max(curr_max , maxi)
                curr_max -= 1
            else:
                continue
        return maxi
            
            
                
        