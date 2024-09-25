from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        cur, res = head, dummy
        while cur and cur.next:
            res.next = cur.next
            cur.next = cur.next.next
            res.next.next = cur
            res = cur
            cur = cur.next
        return dummy.next
    
'''
The `swapPairs` function swaps adjacent nodes in a linked list. Here’s the analysis of 
its time and space complexity:

### Time Complexity
The time complexity is (O(n)), where (n) is the number of nodes in the linked list. 
The function iterates through the list, processing pairs of nodes. Each node is visited
 once, making the time complexity linear.

### Space Complexity
The space complexity is (O(1)). The algorithm uses a constant amount of extra space 
for the pointers (`dummy`, `cur`, `res`) and does not create any additional data 
structures proportional to the input size.

### Summary
- **Time Complexity:** (O(n))
- **Space Complexity:** (O(1))
'''