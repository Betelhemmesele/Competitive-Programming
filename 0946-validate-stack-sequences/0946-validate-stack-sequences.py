class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        n=len(pushed)
        j=0
       
        for i in range(0,n):
            stack.append(pushed[i])
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j=j+1
           
                
                
        return not stack