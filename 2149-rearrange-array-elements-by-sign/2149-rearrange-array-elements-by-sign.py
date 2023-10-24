class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * n
        positive_ind = 0
        negative_ind = 1
        for i in range(n):
            if nums[i] < 0:
                ans[negative_ind] = nums[i]
                negative_ind += 2
            else:
                ans[positive_ind] = nums[i]
                positive_ind += 2
        return ans