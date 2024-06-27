class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        
        if n == 1:
            return 0
        
        hashmap = {}
        
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i , char in enumerate(s):
            if hashmap[char] == 1:
                return i
        
        
        return -1
                    
                    
        