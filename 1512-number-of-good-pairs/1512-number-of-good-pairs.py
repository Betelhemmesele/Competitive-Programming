class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        f = [None] *n  
        visited = -1  
   
        for i in range(0, n):  
            count = 1 
            for j in range(i+1,n):  
                if(nums[i] == nums[j]):
                        count = count + 1 
                        f[j]=visited
            if f[i]!=visited:
                f[i]=count
        for i in range(len(f)):
            if f[i]>1:
                ans+=f[i]*(f[i]-1)//2
        return ans