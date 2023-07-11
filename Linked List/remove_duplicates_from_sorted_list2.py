from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # using hashset or hashmap
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        t1 = head
        d = {}
        while t1:
            if t1.val in d:
                d[t1.val] += 1
            else:
                d[t1.val] = 1
            t1 = t1.next
        new_list = ListNode('')
        t1 = new_list
        for i in d:
            if d[i] == 1:
                t1.next = ListNode(i)
                t1 = t1.next
        return new_list.next

    #in-place
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # construct a dummy node
        dummy.next = head 

        pre = dummy           # set up pre and cur pointers
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
