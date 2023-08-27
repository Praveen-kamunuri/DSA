class Solution(object):
    def findKthPositive(self, arr, k):
        # Get the length of the input array
        n = len(arr)
        
        # Initialize the lower and upper bounds for binary search
        low = 0
        high  = n - 1
        
        # Perform binary search to find the position of kth missing positive integer
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2
            
            # Calculate the count of missing positive integers before the current element
            missing = arr[mid] - (mid + 1)
            
            # If missing count is less than k, adjust the lower bound to search right
            if missing < k:
                low = mid + 1
            else:
                # If missing count is greater than or equal to k, adjust the upper bound to search left
                high = mid - 1
        
        # At this point, high points to the last element before the desired position
        # Calculate the kth missing positive integer by adding k to high
        return k + high + 1
