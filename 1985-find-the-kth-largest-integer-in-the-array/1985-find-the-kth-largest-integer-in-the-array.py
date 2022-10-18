class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        n=len(nums)
       
        nums.sort(key=int)
        large=n-k
        
        return str(nums[large])
            