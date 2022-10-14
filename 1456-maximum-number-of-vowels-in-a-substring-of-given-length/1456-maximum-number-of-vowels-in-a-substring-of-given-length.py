class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       
        vowel=set(['a','e','i','o','u'])
        count=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        x=0
        y=k-1
        mmax=count
        while y < len(s)-1:
            if s[x] in vowel:
                count-=1
            x+=1
            y+=1
            if s[y] in vowel:
                count+=1
            mmax=max(mmax,count)
        return mmax
                    
                    
            