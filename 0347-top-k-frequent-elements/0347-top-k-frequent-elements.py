class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ele_count={}
       
        for ele in nums:
            if ele in ele_count:
                ele_count[ele]+=1
            else:
                ele_count[ele]=1
        
        heap = []
        for i in ele_count:
            heapq.heappush(heap,(-ele_count[i],i))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
            
        return result
        
            
        