class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        ele = None
        for i in range(n):
            if cnt == 0:
                ele = nums[i]
                cnt += 1
            elif nums[i] == ele:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = 0
        for i in range(n):
            if nums[i] == ele:
                cnt1 += 1
        if cnt1 > n // 2:
            return ele
        
        else:
            return -1
                