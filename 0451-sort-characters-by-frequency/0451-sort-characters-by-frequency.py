class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sorted_keys = sorted(hashmap.keys() , key = lambda k: hashmap[k] , reverse = True)
        repeated_keys = [key * hashmap[key] for key in sorted_keys]
        res = ''.join(repeated_keys)
        return res