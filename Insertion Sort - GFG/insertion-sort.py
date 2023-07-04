#Sort the array using insertion sort

class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
            # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]  # Current element to be inserted at the right position
    
            j = i - 1  # Initialize index of the previous element
    
            # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]  # Shift the element to the right
                j -= 1
    
            arr[j + 1] = key  # Insert the current element at the right position


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends