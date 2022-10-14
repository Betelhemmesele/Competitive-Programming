class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        left = n-k
        sum = 0
        totalpts=0
        i =0
        for j in range(k):
            totalpts+=cardPoints[j]
        ans=totalpts
        for i in range(k-1,-1,-1):
            totalpts+=cardPoints[i+left]
            totalpts-=cardPoints[i]
            ans=max(ans,totalpts)
        return ans
            