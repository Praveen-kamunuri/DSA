class Solution:
    def mySqrt(self, x: int) -> int:
        l,h=0,x
        if x<2:return x
        while l<=h:
            m=((l+h)>>1)
            r=m*m
            if r==x:
                return m
            elif r<x:
                l=m+1
            else:
                h=m-1
        return h