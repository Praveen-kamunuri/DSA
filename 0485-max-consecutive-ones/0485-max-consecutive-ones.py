class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if ans < count:
                    ans = count
                count = 0
        return max(ans , count)
        