class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0  # Counter for the number of times the array is rotated
        
        # Iterate through the array to check if it's rotated
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                cnt += 1
        
        # Check the transition between the last and first elements
        if nums[n-1] > nums[0]:
            cnt += 1
        
        # If the counter is less than or equal to 1, it means the array is sorted and rotated
        return cnt <= 1
