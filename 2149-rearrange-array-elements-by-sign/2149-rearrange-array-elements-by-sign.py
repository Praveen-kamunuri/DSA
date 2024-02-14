class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        pos_ind = 0
        neg_ind = 1
        
        for i in range(n):
            if nums[i] < 0:
                ans[neg_ind] = nums[i]
                neg_ind += 2
            else:
                ans[pos_ind] = nums[i]
                pos_ind += 2
        return ans
        