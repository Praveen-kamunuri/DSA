#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        return min_ind
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min_ind = self.select(arr, i)
            if i != min_ind:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends