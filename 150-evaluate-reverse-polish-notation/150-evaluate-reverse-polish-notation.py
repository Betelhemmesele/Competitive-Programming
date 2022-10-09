class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=['+','-','*','/']
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                y,x=stack.pop(),stack.pop()
                if i==op[0]:
                    stack.append(x+ y)
                elif i==op[1]:
                    stack.append(x - y)
                elif i==op[2]:
                    stack.append(x * y)
                else:
                    stack.append(trunc(x/y))
        return stack[0]
        