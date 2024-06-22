class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        
        k = k % n
        
        rotated = [0] * n# [0,0,0,0,0,0,0]
        
        for i in range(n):
            rotated[(i+k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]
            
        
        
        