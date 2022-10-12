class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        Len=len(nums)
        prefix=[0]*(Len+1)
        odd=0
        for i in range(Len):
            prefix[odd]+=1
            if nums[i]&1:
                odd+=1
            if odd>=k:
                count+=prefix[odd-k]
        return count