class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def solve_spc_opt(arr):
            m = len(arr)
            
            prev = arr[0]
            prev2 = 0

            for i in range(1, m):
                take = arr[i]

                if i > 1:
                    take += prev2
                not_take = 0 + prev

                curr = max(take, not_take)

                prev2 = prev
                prev = curr
            return prev
        
        first_take = solve_spc_opt(nums[:-1])
        last_take = solve_spc_opt(nums[1:])

        return max(first_take, last_take)
        