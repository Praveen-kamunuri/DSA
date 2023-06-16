class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        num_str = str(x)
        l = ""
        for i in range(len(num_str)-1,-1,-1):
            l = l+num_str[i]
        digit = int(l)
        if digit > 2**31 -1:
            return 0
        
        return  sign * digit
        