class Solution:
    def beautySum(self, s: str) -> int:
        def freq(string):
            hashmap = {}
            for i in string:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            maxi = max(hashmap.values())
            mini = min(hashmap.values())
            return maxi - mini
            
        
        
        
        
        
        total_sum = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                sub_str = s[i:j+1]
                curr_freq = freq(sub_str)
                total_sum += curr_freq
        return total_sum
                