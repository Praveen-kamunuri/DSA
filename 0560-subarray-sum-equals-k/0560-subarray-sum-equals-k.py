class Solution(object):
    def subarraySum(self, nums, k):
        hashmap = {}
        n = len(nums)
        cur_sum = 0
        count = 0  # Initialize the count of subarrays whose sum equals k

        for i in range(n):
            cur_sum += nums[i]
            if cur_sum == k:
                count += 1
            
            if cur_sum - k in hashmap:
                count += hashmap[cur_sum - k]
            
            hashmap[cur_sum] = hashmap.get(cur_sum, 0) + 1

        return count
