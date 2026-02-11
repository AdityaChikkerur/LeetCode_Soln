# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        if head==None or head.next==None:
            return head
        evenhead=head.next
        oddhead=head
        evenp=head.next
        oddp=head
        while oddp.next!=None and evenp.next!=None:
            oddp.next=oddp.next.next
            oddp=oddp.next
            evenp.next=evenp.next.next
            evenp=evenp.next
        oddp.next=evenhead
        return head