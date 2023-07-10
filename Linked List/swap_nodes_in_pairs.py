from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        cur, res = head, dummy
        while cur and cur.next:
            res.next = cur.next
            cur.next = cur.next.next
            res.next.next = cur
            res = cur
            cur = cur.next
        return dummy.next