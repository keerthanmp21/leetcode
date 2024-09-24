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
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
'''
The `addTwoNumbers` function adds two numbers represented by two linked lists. 
Here's the time and space complexity analysis for this function:

### Time Complexity
The time complexity of the function is (O(max(m, n))), 
where (m) is the length of the first linked list (`l1`) and (n) is the length of the 
second linked list (`l2`). This is because we traverse both lists completely at most 
once, processing each node and any carry.

### Space Complexity
The space complexity is (O(max(m, n))) as well, because we create a new linked list 
to store the result. The size of this result list can be at most the length of the 
longer input list plus one additional node in case of a carry at the end.

### Summary
- **Time Complexity:** (O(max(m, n)))
- **Space Complexity:** (O(max(m, n)))
'''
