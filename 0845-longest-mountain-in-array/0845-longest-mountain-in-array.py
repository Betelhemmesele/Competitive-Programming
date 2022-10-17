class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        n=len(arr)
        
        output=0
        for i in range(1,n-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                count=1
                j=i
                while j>0 and arr[j]>arr[j-1]:
                    j-=1
                    count+=1
                while i<n-1 and arr[i]>arr[i+1]:
                    i+=1
                    count+=1
                output=max(output,count)
            else:
                i+=1
        return output
            
                
            
        