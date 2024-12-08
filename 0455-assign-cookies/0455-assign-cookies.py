class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        n = len(g)
        
        m = len(s)
        
        g.sort()
        
        s.sort()
        
        left = 0
        
        right = 0
        
        while left < m and right < n:
            if g[right] <= s[left]:
                right += 1
            
            left += 1
        
        return right