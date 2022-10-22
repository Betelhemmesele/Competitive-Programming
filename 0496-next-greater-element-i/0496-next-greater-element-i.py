class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        n=len(nums2)
        res=[-1]*len(nums1)
        
        for i in range(n):
            cur=nums2[i]
            
            while arr and cur > arr[-1]:
                val=arr.pop()
                ind=nums1.index(val)
                res[ind]=cur
            if cur in nums1:
                arr.append(cur)
        return res
            
            
            