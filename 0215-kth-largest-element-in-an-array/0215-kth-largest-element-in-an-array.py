class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        cnt = 1
        for i in range(n-1, -1, -1):
            if cnt == k:
                return nums[i]
            else:
                cnt += 1
        
            