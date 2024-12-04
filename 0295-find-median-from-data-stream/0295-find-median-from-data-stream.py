class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()  # Sort the array every time before finding the median
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n // 2]
        else:
            mid = n // 2
            return (self.arr[mid - 1] + self.arr[mid]) / 2.0
