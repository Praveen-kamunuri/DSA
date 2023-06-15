#User function Template for python3
class Solution:
    def print2largest(self, arr, n):
        largest = arr[0]
        slargest = -1
        for i in range(1, len(arr)):
            if arr[i] > largest:
                slargest = largest
                largest = arr[i]
            elif largest > arr[i] > slargest:
                slargest = arr[i]
        return slargest

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends