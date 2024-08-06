class Pair:
    def __init__(self, x, y):
        # Initialize Pair with element value and current minimum value
        self.ele = x
        self.minVal = y

class MinStack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, val: int) -> None:
        # Determine the minimum value to store
        if not self.stack:
            min_val = val
        else:
            min_val = min(self.stack[-1].minVal, val)
        
        # Push the new value and current minimum as a Pair
        self.stack.append(Pair(val, min_val))
        # Time Complexity: O(1) - comparison and append operation are constant time
        # Space Complexity: O(1) per operation, but O(n) overall where n is the number of elements pushed onto the stack

    def pop(self) -> None:
        # Pop the top element from the stack
        self.stack.pop()
        # Time Complexity: O(1) - pop operation is constant time
        # Space Complexity: O(1) - no additional space required

    def top(self) -> int:
        # Return the element value of the top Pair
        top_ele = self.stack[-1].ele
        return top_ele
        # Time Complexity: O(1) - accessing the top element is constant time
        # Space Complexity: O(1) - no additional space required

    def getMin(self) -> int:
        # Return the current minimum value from the top Pair
        min_ele = self.stack[-1].minVal
        return min_ele
        # Time Complexity: O(1) - accessing the minimum element is constant time
        # Space Complexity: O(1) - no additional space required

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
