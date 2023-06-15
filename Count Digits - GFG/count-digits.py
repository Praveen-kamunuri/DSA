#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # Convert N to a string
        N_str = str(N)
    
        # Initialize count to 0
        count = 0
    
        # Iterate through each digit
        for digit_char in N_str:
            # Convert digit back to an integer
            digit = int(digit_char)
        
            # Check if the digit is not zero and evenly divides N
            if digit != 0 and N % digit == 0:
                count += 1
    
        return count




            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends