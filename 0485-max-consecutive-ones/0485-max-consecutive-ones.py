class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        
        start = -1
        for i in range(n):
            if nums[i] == 1:
                start = i
                break
        if start == -1:
            return 0
        print("s",start)
        cnt = 1
        maxi = 1
        for i in range(start + 1 ,n):
            if nums[i] == 1:
                cnt += 1
            else:
                maxi = max(maxi , cnt)
                cnt = 0
        maxi = max(maxi , cnt)
        return maxi
        