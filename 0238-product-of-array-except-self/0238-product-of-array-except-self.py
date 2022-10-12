class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Len=len(nums)
        L=[1]*Len
        R=[1]*Len
        res=[]
        for i in range(1,Len):
            L[i]=L[i-1]*nums[i-1]
        for i in range (Len-2, -1, -1):
            R[i]=R[i+1]*nums[i+1]
        for i in range(0,Len):
            res.append(L[i]*R[i])
        return res