from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        ans = [False] * len(queries)
        
        # Create an array to store if adjacent elements have different parity
        arr = [nums[i] % 2 != nums[i + 1] % 2 for i in range(n - 1)]
        
        # Prefix sum array to count special pairs
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if arr[i - 1] else 0)
        
        # Answer each query
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]
            num = prefix_sum[right] - prefix_sum[left]
            ans[i] = (num == (right - left))
        
        return ans
