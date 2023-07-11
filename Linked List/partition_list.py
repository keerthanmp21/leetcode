from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = temp1 = ListNode(0)
        head2 = temp2 = ListNode(0)
        while head:
            if head.val < x:
                temp1.next = head
                temp1 = temp1.next
            else:
                temp2.next = head
                temp2 = temp2.next
            head = head.next
        temp2.next = None
        temp1.next = head2.next
        return head1.next