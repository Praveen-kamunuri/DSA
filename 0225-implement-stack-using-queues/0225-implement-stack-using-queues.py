from collections import deque

class MyStack:

    def __init__(self):
        # Initialize two deques (queues)
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Append element x to queue1
        self.queue1.append(x)

    def pop(self) -> int:
        # Move elements from queue1 to queue2, except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # The last element in queue1 is the top element of the stack
        popped_element = self.queue1.popleft()
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self) -> int:
        # Move elements from queue1 to queue2, except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # The last element in queue1 is the top element of the stack
        top_element = self.queue1.popleft()
        # Save the top element to return after pushing it back to queue2
        self.queue2.append(top_element)
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self) -> bool:
        # Return True if queue1 is empty, else False
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()