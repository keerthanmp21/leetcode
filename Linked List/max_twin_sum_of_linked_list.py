from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        # get mid node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nxt = prev = None
        # reverse second half
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        res = 0
        # find sum of twin and update res
        while prev:
            res = max(res, head.val + prev.val)
            prev = prev.next
            head = head.next

        return res
