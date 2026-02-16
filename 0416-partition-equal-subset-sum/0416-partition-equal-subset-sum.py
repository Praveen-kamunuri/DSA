class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        total_sum = 0

        for i in range(n):
            total_sum += nums[i]
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        def find_equal_subset_sum(ind, target):

            if target == 0:
                return True

            if ind == 0:
                return False

            take = False

            if nums[ind] <= target:
                take = find_equal_subset_sum(ind - 1, target - nums[ind])
            
            not_take = find_equal_subset_sum(ind - 1, target)

            return take or not_take

        return find_equal_subset_sum(n - 1, target)

