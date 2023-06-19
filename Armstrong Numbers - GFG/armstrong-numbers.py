#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here 
        res = 0
        num_char = str(n)
        for i in range(len(num_char)):
            res = res + int(num_char[i]) ** 3
        if res == n:
            return "Yes"
        else:
            return "No"
            


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