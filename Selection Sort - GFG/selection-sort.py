#User function Template for python3
class Solution:
    def selectionSort(self, arr, N):
        # Iterate through the array
        for i in range(N-1):
            # Assume the current index as the minimum
            min = i
            
            # Find the minimum element in the remaining unsorted portion
            for j in range(i+1, N):
                # If a smaller element is found, update the minimum index
                if arr[j] < arr[min]:
                    min = j
            
            # Swap the minimum element with the current element
            arr[i], arr[min] = arr[min], arr[i]

                
                
            


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