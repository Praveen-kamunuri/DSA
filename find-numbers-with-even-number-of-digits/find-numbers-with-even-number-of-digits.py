class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            str_num = str(i)
            if len(str_num) % 2 == 0:
                cnt += 1
        return cnt
        