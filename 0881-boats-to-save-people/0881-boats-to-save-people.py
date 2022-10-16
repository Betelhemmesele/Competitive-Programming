class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        begin=0
        end=len(people)-1
        boats=0
        while begin<=end:
            boats+=1
            weight=people[begin]+people[end]
            if weight<=limit:
                begin+=1
            end-=1
        return boats
                
            