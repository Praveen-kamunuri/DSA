class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        
            
        
        hashmap = { 
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
            
        }
        
        def generate(ind, path):
            
            if ind == len(digits):
                ans.append(''.join(path))
                return
            
            curr_letter = digits[ind]
            letters = hashmap[curr_letter]
            
            for i in letters:
                path.append(i)
                generate(ind + 1, path)
                path.pop()
                
                
        
        ans = []
        generate(0, [])
        return ans
        