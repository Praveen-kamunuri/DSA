from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize an empty list to store the result
        res = []
        
        # Initialize a deque (double-ended queue) to store indices of useful elements
        q = deque()
        
        # Iterate over the entire list
        for i in range(n):
            # If the deque is not empty and the leftmost index is out of the current window, remove it
            if q and q[0] <= i - k:
                q.popleft()
            
            # Maintain the deque to store only useful elements by removing smaller elements from the right
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            # Append the current element's index to the deque
            q.append(i)
            
            # Once the window reaches size k, add the maximum element (at q[0]) to the result list
            if i >= k - 1:
                res.append(nums[q[0]])
        
        # Return the list of maximum values for each sliding window
        return res
