# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # b=[]
        # while head!=None:
        #     b.append(head.val)
        #     head=head.next
        # if b==b[::-1]:
        #     return True
        # return False


        if head==None and head.next!=None:
            return head

        #find middle 
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        # print(slow)
        cur=slow
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        # print(prev)

        # Compare two halves
        first=head
        second=prev
        while second!=None and first!=None:
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        return True
