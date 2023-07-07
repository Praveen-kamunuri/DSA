#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        d = d % n
        li = []
        for i in range(d+1):
            li.append(arr[i])
        for i in range(d,n):
            arr[i-d] = arr[i]
        k = n-d
        for i in range(n-d,n):
            arr[i] = li[k - (n - d)]
            k += 1
        return arr
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends