class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        Len=len(nums)
        for i in range(Len):
            if nums[i]!=0:
                nums[count]=nums[i]
                count+=1
        while count < Len:
            nums[count]=0
            count+=1