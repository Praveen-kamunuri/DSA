class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        temp = 0
        
        for i in range(n):
            if nums[i] == val:
                temp += 1
            else:
                nums[i - temp] = nums[i]
        
        return n - temp
