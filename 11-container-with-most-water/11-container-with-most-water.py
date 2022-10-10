class Solution:
    def maxArea(self, height: List[int]) -> int:
            area=0
            Len=len(height)
            fi=0
            la=Len-1
            while(fi<la):
                if height[fi] > height[la]:
                    x=height[la]
                else:
                    x=height[fi]
                area=max(x*(la-fi),area)
                if height[fi] < height[la]:
                    fi+=1
                else: 
                    la-=1
            return area