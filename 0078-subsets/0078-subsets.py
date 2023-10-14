from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for num in range(1 << n):
            sub = []
            for i in range(n):
                if num & (1 << i):
                    sub.append(nums[i])
            ans.append(sub)

        return ans
