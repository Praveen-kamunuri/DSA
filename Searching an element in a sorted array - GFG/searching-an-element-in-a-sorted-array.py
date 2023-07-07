#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self, arr, N, K):
        # Your code here
        i = 0  # Initialize index variable to 0
        while (i < N):  # Start a while loop with the condition (i < N)
            if arr[i] != K:  # Check if element at index i is not equal to K
                i += 1  # Increment i by 1 if the element is not equal to K
            elif arr[i] == K:  # Check if element at index i is equal to K
                return 1  # Return 1 if the element is found
        return -1  # Return -1 if the element is not found

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends