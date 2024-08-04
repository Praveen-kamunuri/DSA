class MyQueue:

    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def push(self, x: int) -> None:
        # Push the element onto stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        self.transfer()
        # Pop the element from stack_out
        pop_element = self.stack_out.pop()
        return pop_element

    def peek(self) -> int:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        self.transfer()
        # Return the top element of stack_out without popping it
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Return True if both stack_in and stack_out are empty, otherwise False
        return not self.stack_in and not self.stack_out

    def transfer(self):
        # Move elements from stack_in to stack_out if stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Example usage:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
