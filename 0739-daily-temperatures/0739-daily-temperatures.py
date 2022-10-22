class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[]
        n=len(temperatures)
        res=[0]*n
        
        for i in range(0,n):
            while (len(arr)>0) and temperatures[i]> temperatures[arr[len(arr)-1]]:
                    jex=arr[len(arr)-1]
                    arr.pop()
                    res[jex] = i-jex
            arr.append(i)
        return list(res)
        
            