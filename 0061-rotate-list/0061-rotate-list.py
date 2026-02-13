# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        temp=None
        if head==None or head.next==None:
            return head
        len=1
        while cur.next!=None:
            len+=1
            cur=cur.next
            
        cur=head
        for i in range(0,k % len):
            cur=head
            while cur.next!=None and cur.next.next!=None:
                cur=cur.next

            temp=cur.next
            temp.next=head          
            cur.next=None
            head=temp
        return head
                
