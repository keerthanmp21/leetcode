from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1 = head
        odd_list = ListNode('')
        odd_temp = odd_list
        even_list = ListNode('')
        even_temp = even_list
        is_odd = True
        is_even = False
        while t1:
            if is_odd:
                is_odd = False
                is_even = True
                odd_temp.next = ListNode(t1.val)
                odd_temp = odd_temp.next
            elif is_even:
                is_even = False
                is_odd = True
                even_temp.next = ListNode(t1.val)
                even_temp = even_temp.next
            t1 = t1.next
        even_list = even_list.next
        odd_list = odd_list.next
        odd_temp.next = even_list
        return odd_list

    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head