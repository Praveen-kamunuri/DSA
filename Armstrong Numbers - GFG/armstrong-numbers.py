#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber(ob, n):
        res = 0  # Initialize the variable to store the sum of cube values
        num_char = str(n)  # Convert the number to a string to access individual digits

        # Iterate through each digit in the number
        for i in range(len(num_char)):
            res += int(num_char[i]) ** 3  # Calculate the cube of the digit and add it to the sum

        # Check if the sum of cube values is equal to the original number
        if res == n:
            return "Yes"  # Return "Yes" if it is an Armstrong number
        else:
            return "No"  # Return "No" if it is not an Armstrong number

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends