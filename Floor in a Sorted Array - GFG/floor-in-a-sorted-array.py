class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, A, N, X):
        low = 0
        high = N - 1
        ans = N
        # Check if X is smaller than the first element in the array
        if X < A[0]:
            return -1
        # Check if X is greater than the last element in the array
        if X > A[high]:
            return high
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == X:
                return mid
            elif A[mid] >= X:
                ans = mid
                high = mid - 1  # Discard the upper half of the array
            else:
                low = mid + 1  # Discard the lower half of the array
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends