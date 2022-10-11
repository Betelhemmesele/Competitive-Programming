class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        length=len(nums)
        for i in range(0,length):
            sum+=nums[i]
        left=0
        for i in range(0,length):
            right=sum-nums[i]-left
            if left==right:
                return i
            left+=nums[i]
        return -1
        