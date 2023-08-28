from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        total_length = 1
        tail = head
        # get the length of the list and the last node in the list
        while tail.next:
            total_length += 1
            tail = tail.next

        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        tail.next = head

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % total_length
        cur = head
        # Traverse the list to get to the node just before the ( length - k )th node.
        for _ in range(total_length - k - 1):
            cur = cur.next

        output = cur.next
        cur.next = None
        return output
