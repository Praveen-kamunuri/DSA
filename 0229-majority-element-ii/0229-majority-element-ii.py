class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        mini = floor(n/3) 
        hashmap = {}
        result = []
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] > mini and i not in result:
                result.append(i)
        return result
        