# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head
        while(p1 and p1.next):
            p1=p1.next.next
            p2=p2.next
        return p2