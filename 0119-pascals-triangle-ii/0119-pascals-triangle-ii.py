class Solution:
    def __init__(self):
        self.factList={0:1,1:1}
    def fact(self,n):
        if n not in self.factList:
            self.factList[n]=self.fact(n-1)*n
        return self.factList[n]
    def ncr(self,n,r):
        return self.fact(n)//(self.fact(n-r)*self.fact(r))
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        for i in range(rowIndex+1):
            res.append(self.ncr(rowIndex,i))
        return res