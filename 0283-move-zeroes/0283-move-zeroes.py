class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        zeros_cnt = 0
        for i in nums:
            if i != 0:
                res.append(i)
            else:
                zeros_cnt += 1
        for i in range(zeros_cnt):
            res.append(0)
        for i in range(len(res)):
            nums[i] = res[i]
            
                
        