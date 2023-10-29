class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []  # Initialize the result list

        for i in range(n):
            # Skip duplicate values at the same position
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # Skip duplicate values at the same position
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    summ = nums[i] + nums[j] + nums[k] + nums[l]

                    if summ == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        res.append(temp)
                        k += 1
                        l -= 1

                        # Skip duplicate values at new positions
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif summ < target:
                        k += 1
                    else:
                        l -= 1

        return res  # Return the list of lists containing four numbers that sum to the target.
