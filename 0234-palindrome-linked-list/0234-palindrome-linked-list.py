# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        b=[]
        while head!=None:
            b.append(head.val)
            head=head.next
        if b==b[::-1]:
            return True
        return False