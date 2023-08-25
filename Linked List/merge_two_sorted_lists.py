from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative
    def mergeTwoLists1(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list3 = ListNode("")
        t1 = list1
        t2 = list2
        t3 = list3

        while t1 and t2:
            if t1.val < t2.val:
                t3.next = ListNode(t1.val)
                t1 = t1.next
            else:
                t3.next = ListNode(t2.val)
                t2 = t2.next
            t3 = t3.next

        if t1:
            t3.next = t1
        if t2:
            t3.next = t2
        return list3.next

    # recursive
    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
