class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        con=0
        j=0
        zerocount=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                zerocount+=1
            while zerocount > k:
                if nums[j]==0:
                    zerocount-=1
                j+=1
            con=max(con,i-j+1)
        return con