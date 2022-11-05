class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index=len(nums)
        output=[]
        sorte=[0]*index
        for i in range(0,index):
            sorte[i]=nums[i]
        sorte.sort()
        for i in range(0,index):
            hh=sorte.index(nums[i])
            output.append(hh)
        return output