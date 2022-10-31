class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        ele_count={}
       
        for ele in arr:
            if ele in ele_count:
                ele_count[ele]+=1
            else:
                ele_count[ele]=1
        val=sorted(ele_count.values(),reverse=True)
        l=len(arr)
        r=l//2
        remv=0
        for count in val:
            r-=count
            remv+=1
            if r<=0:
                return remv
        return remv
            
            