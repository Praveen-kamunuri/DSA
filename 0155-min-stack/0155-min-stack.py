class Pair:
    
    def __init__(self, x, y):
        self.ele = x
        self.minVal = y



class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val
        else:
            min_val = min(self.stack[-1].minVal, val)
        
        self.stack.append(Pair(val, min_val))
        
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        top_ele = self.stack[-1].ele
        return top_ele
        

    def getMin(self) -> int:
        min_ele = self.stack[-1].minVal
        return min_ele
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()