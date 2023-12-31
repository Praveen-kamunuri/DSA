from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for r in range(n + 1):
            subsets = set(combinations(nums, r))
            ans.extend(list(subsets))

        return ans

    