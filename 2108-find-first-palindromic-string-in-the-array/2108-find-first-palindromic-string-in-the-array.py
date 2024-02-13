class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def ispal(string):
            n = len(string)
            i = 0
            j = n - 1
            
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        
        
        n = len(words)
        
        for i in range(n):
            if ispal(words[i]):
                return words[i]
        return ""
            