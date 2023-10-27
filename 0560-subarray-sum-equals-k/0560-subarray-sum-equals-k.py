class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        n = len(nums)
        cnt = 0
        pre_sum = 0
        hashmap[0] = 1
        for i in range(n):
            pre_sum += nums[i]
            remove = pre_sum - k
            cnt += hashmap[remove]
            hashmap[pre_sum] += 1
        return cnt
            