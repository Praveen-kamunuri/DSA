#User function Template for python3

class Solution:
    def select(self, arr, i):
        # Find the index of the minimum element in arr starting from index i
        min_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        return min_ind
    
    def selectionSort(self, arr,n):
        # Perform selection sort on the arr
        for i in range(len(arr)):
            # Find the index of the minimum element from i to the end
            min_ind = self.select(arr, i)
            # If the minimum element is not already at its correct position
            if i != min_ind:
                # Swap the elements at indices i and min_ind
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