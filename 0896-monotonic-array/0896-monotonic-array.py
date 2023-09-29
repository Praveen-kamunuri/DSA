class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc , dec = True , True
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                dec = False
            if nums[i+1] < nums[i]:
                inc = False
        return inc or dec
        