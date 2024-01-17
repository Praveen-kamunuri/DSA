class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            
        hashSet = set()
        flag = True
        for count in hashmap.values():
            if count in hashSet:
                flag = False
                break
            else:
                hashSet.add(count)
        
        return flag
                
        