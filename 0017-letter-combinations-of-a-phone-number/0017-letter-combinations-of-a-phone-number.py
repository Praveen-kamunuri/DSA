class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        
        def backtrack(ind, ds):
            
            if ind == n:
                res.append(''.join(ds))
                return
            
            
            curr_digit = digits[ind]
            
            letters = hashmap[curr_digit]
            
            for letter in letters:
                ds.append(letter)
                backtrack(ind + 1, ds)
                ds.pop()
                
        
        
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
        
        n = len(digits)
        
        res = []
        ds = []
        backtrack(0, ds)
        
        return res
        
        
        
        