class MinStack:
    
    def __init__(self):
        self.stack = [] 
        self.min_stack = []
         
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        remove_item = self.stack.pop()
        if remove_item == self.min_stack[len(self.stack)-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) #// return -3
minStack.pop()
print(minStack.top())  # // return 0
print(minStack.getMin()) #// return -2