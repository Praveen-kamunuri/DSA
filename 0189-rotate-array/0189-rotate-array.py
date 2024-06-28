class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        
        k = k % n
        
        nums[:] = nums[::-1]
        
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums