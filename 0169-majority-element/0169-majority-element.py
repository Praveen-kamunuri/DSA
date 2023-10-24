class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        ele = None
        
        # Voting Algorithm:
        # Find the majority candidate.
        for i in range(n):
            if cnt == 0:
                ele = nums[i]  # Set the current element as the potential majority candidate.
                cnt += 1
            elif nums[i] == ele:
                cnt += 1  # Increment count for the current candidate.
            else:
                cnt -= 1  # Decrement count for a different element.
        
        cnt1 = 0
        
        # Count the occurrences of the potential majority candidate.
        for i in range(n):
            if nums[i] == ele:
                cnt1 += 1
        
        # If the potential majority candidate occurs more than n // 2 times, it is the majority element.
        if cnt1 > n // 2:
            return ele
        else:
            return -1  # No majority element found.
