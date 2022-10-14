class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        k=0
        output=0
        for j in range(len(nums)):
            if nums[j]==0:
                k+=1
            while k>1:
                if nums[i]==0:
                    k-=1
                i+=1
            output=max(output,j-i)
        return output