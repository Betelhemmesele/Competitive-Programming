class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        start=0
        end=0
        maxcount=0
        output=set()
        while end < n:
            if s[end] not in output:
                output.add(s[end])
                end+=1
                maxcount=max(maxcount,len(output))
            else:
                output.remove(s[start])
                start+=1
        return maxcount