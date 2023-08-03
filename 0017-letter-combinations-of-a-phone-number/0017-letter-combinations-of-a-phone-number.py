class Solution(object):
    def letterCombinations(self, digits):
        hashmap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        li = []
        for d in digits:
            if not li:
                li.extend(hashmap[d])
                continue
            arr = []
            for i in li:
                for j in hashmap[d]:
                    arr.append(i+j)
            li = arr
        return li
        
        