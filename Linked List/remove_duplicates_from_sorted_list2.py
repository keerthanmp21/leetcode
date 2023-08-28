from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # using hashset or hashmap
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        no_of_occ = {}
        cur = head
        while cur:
            if cur.val in no_of_occ:
                no_of_occ[cur.val] += 1
            else:
                no_of_occ[cur.val] = 1
            cur = cur.next

        res = ListNode('')
        t1 = res
        for k, v in no_of_occ.items():
            if v == 1:
                t1.next = ListNode(k)
                t1 = t1.next
        
        return res.next

    # in-place
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # construct a dummy node
        dummy.next = head

        pre = dummy  # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                # this will be verified by next line
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
