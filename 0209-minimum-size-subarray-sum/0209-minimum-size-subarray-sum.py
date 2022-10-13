class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        sums=0
        minlen=float("inf")
        for i in range(n):
            sums+=nums[i]
            while sums >= target:
                out=i-j+1
                if out< minlen:
                    minlen=out
                sums-=nums[j]
                j+=1
            i+=1
        return minlen if not minlen==float("inf") else 0
                
                
                
                
                
        
        