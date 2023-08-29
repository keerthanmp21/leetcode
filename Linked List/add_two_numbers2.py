from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        s1 = ""
        t1 = l1
        s2 = ""
        t2 = l2
        while t1 or t2:
            if t1:
                s1 += str(t1.val)
                t1 = t1.next
            if t2:
                s2 += str(t2.val)
                t2 = t2.next

        sum_val = int(s1) + int(s2)

        l3 = ListNode("")
        t3 = l3
        for i in str(sum_val):
            node = ListNode(i)
            t3.next = node
            t3 = t3.next
        return l3.next
