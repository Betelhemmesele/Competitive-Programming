class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n=len(nums)
        k=len(r)
        
        output=[]
        for i in range(k):
            output.append(self.checkcurrentarray(nums,l[i],r[i]+1))
        return output
        
    def checkcurrentarray(self,nums,n,m):
        sequence=[]
        for i in range(n,m):
            sequence.append(nums[i])
        sequence.sort()
        for j in range(2, len(sequence)):
            if sequence[j] - sequence[j-1] != sequence[1]-sequence[0]:
                return False
        return True