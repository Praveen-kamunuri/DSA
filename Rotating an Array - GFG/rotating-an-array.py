#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        
        # Calculate the effective number of rotations
        d = d % n
        
        # Create an empty list to store the elements to be shifted
        li = []
        
        # Store the first d+1 elements in the list
        for i in range(d+1):
            li.append(arr[i])
        
        # Shift the remaining elements by d positions to the left
        for i in range(d, n):
            arr[i-d] = arr[i]
        
        # Calculate the starting index for placing the shifted elements
        k = n-d
        
        # Place the shifted elements at the end of the array
        for i in range(n-d, n):
            arr[i] = li[k - (n - d)]
            k += 1
        
        # Return the modified array
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