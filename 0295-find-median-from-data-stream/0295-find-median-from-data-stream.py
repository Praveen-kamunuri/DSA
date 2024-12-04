class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        
        if n == 1:
            return self.arr[0]
        
        if n % 2 == 1:
            return self.arr[n//2]
        else:
            mid = (n // 2) 
            
            return (self.arr[mid - 1] + self.arr[mid]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()