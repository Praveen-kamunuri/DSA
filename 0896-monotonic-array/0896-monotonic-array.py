class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc, dec = True, True  # Initialize both flags to True

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dec = False  # If we find an increasing pair, set dec to False
            elif nums[i] < nums[i-1]:
                inc = False  # If we find a decreasing pair, set inc to False

        # If either flag is True, it means the list is monotonic
        return inc or dec
