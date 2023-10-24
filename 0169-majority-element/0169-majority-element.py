class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maj = n // 2
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for key , val in hashmap.items():
            if val > maj:
                return key
            