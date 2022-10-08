class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index=len(nums)
        output=[0]*index
        no=0
        index=len(nums)
        for i in range(index):
            for j in range(index):
                if j!=i and nums[j]<nums[i]:
                    output[i]+=1       
        return output       
        