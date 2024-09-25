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

'''
The `rotateRight` function rotates a linked list to the right by (k) places. 
Let's analyze its time and space complexity.

### Time Complexity
The time complexity of this function is (O(n)), where (n) is the number of nodes in 
the linked list. The function performs the following operations:
1. It traverses the linked list once to find the total length and the tail of the list
(which takes (O(n))).
2. It computes the effective rotations needed (`k % total_length`).
3. It traverses the list again to find the new tail (which takes another (O(n)) in
 the worst case).

Since both key operations are linear with respect to the number of nodes, the overall
 time complexity remains (O(n)).

### Space Complexity
The space complexity is (O(1)) because the function uses a constant amount of extra space. 
It only utilizes a few pointers (`total_length`, `tail`, `cur`, and `output`), 
regardless of the size of the linked list.

### Summary
- **Time Complexity:** (O(n))
- **Space Complexity:** (O(1))
'''