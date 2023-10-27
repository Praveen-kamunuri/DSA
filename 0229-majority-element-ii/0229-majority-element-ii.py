class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        maj = n // 3
        hashmap = {}
        for i in  nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for key , val in hashmap.items():
            if val > maj:
                res.append(key)
        return res
                
        