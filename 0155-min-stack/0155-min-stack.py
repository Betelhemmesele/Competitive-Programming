class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self,val:int):
        self.stack.append(val)
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
    def getMin(self):
        if self.stack:
            minn=self.stack[0]
        for i in range(1,len(self.stack)):
            if self.stack[i]<minn:
                minn=self.stack[i]
        return minn
            
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()