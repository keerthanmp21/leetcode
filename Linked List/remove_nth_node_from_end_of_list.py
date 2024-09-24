from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:# if n = 1 and head has 1 value
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

'''
The `removeNthFromEnd` function removes the nth node from the end of a singly-linked list. 
Let's analyze its time and space complexity:

### Time Complexity
The time complexity is (O(L)), where (L) is the length of the linked list. 
The algorithm involves:
1. Moving the `fast` pointer (n) steps ahead.
2. Then, moving both `fast` and `slow` pointers until `fast` reaches the end of the 
list. This traversal takes linear time with respect to the length of the list.

### Space Complexity
The space complexity is (O(1)). The function uses a constant amount of extra space 
regardless of the input size because it only uses a few pointers (`fast`, `slow`) and
 does not create any new data structures proportional to the input size.

### Summary
- **Time Complexity:** (O(L))
- **Space Complexity:** (O(1))
'''