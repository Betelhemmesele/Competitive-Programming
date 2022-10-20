class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        while len(self.stk1) != 0:
            self.stk2.append(self.stk1[-1])
            self.stk1.pop()
 
        # Push item into self.s1
        self.stk1.append(x)
 
        # Push everything back to s1
        while len(self.stk2) != 0:
            self.stk1.append(self.stk2[-1])
            self.stk2.pop()
            
        

    def pop(self) -> int:
        if self.stk1:
            return self.stk1.pop()

    def peek(self) -> int:
        if self.stk1:
            return self.stk1[-1]

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2

    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
