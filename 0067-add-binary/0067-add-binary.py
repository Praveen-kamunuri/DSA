class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        res=""
        i=0
        c=0
        while i<min(len(a),len(b)):
            if a[i]=='1' and b[i]=='1':
                if c==1:
                    res+='1'
                else:
                    res+='0'
                    c=1
            elif a[i]=='1' or b[i]=='1':
                if c==1:
                    res+='0'
                else:
                    res+='1'
            else:
                if c==1:
                    res+='1'
                    c=0
                else:
                    res+='0'
            i+=1
        while i<len(a):
            if a[i]=='1':
                if c==1:
                    res+='0'
                else:
                    res+='1'
            else:
                if c==1:
                    res+='1'
                    c=0
                else:
                    res+='0'
            i+=1
        while i<len(b):
            if b[i]=='1':
                if c==1:
                    res+='0'
                else:
                    res+='1'
            else:
                if c==1:
                    res+='1'
                    c=0
                else:
                    res+='0'
            i+=1
        res+=str(c)
        return str(int(res[::-1]))