class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
            n=len(nums)
            nums.sort()
            output=[]
            for i in range(0,n):
                if target==nums[i]:
                    output.append(i)
            return output
                
            
            