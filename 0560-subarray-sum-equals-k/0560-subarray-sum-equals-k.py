class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output=0
        csum=0
        presum={0:1}
        for n in nums:
            csum+=n
            dif=csum-k
            output+=presum.get(dif,0)
            presum[csum]=1+presum.get(csum,0)
        return output
        
    
        