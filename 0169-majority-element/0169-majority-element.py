class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        target = len(nums) // 2
        for ele in nums:
            if ele in hashmap:
                hashmap[ele] += 1
            else:
                hashmap[ele] = 1
        for ele , value in hashmap.items():
            if value > target:
                return ele
        