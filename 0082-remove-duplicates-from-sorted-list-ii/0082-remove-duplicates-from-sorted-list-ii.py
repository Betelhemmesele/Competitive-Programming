# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        c=Counter(arr) 
        arr=[key for key,val in c.items() if val==1]
        gig=cur=ListNode()
        for i in arr:
            cur.next=ListNode(i)
            cur=cur.next
        return gig.next    
            
            
            