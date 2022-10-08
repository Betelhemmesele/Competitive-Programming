class Solution:
    def sortSentence(self, s: str) -> str:
        lists=s.split()
        output=[]
        wordorder={}
        for li in lists:
            order=int(li[-1])
            wordorder[order]=li[:-1]
        for i in range(1,len(lists)+1):
            new=wordorder[i]
            output.append(new)
        
            
        return " ".join(output)
    
        
    
        
        