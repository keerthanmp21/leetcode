from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_nodes = 0
        t1 = head
        while t1:
            total_nodes += 1
            t1 = t1.next
        first = head
        second = head
        t1 = head
        curr_node = 1
        while t1:
            if curr_node == k:
                first = t1
            if curr_node == total_nodes - k + 1:
                second = t1
            curr_node += 1
            t1 = t1.next
        first.val, second.val = second.val, first.val
        return head
