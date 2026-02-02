
class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        n = len(nums)

        res = nums[0]

        first_min = 51
        sec_min = 51

        for i in range(1, n):
            if nums[i] < first_min:
                sec_min = first_min
                first_min = nums[i]
            elif nums[i] < sec_min:
                sec_min = nums[i]

        return res + first_min + sec_min