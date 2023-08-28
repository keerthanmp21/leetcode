from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative approach1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp

        return prev

    # iterative approach 2
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    # recursive approach
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
