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


'''
=>iterative
The `mergeTwoLists` function merges two sorted linked lists into a single sorted 
linked list. Here’s the analysis of its time and space complexity:

### Time Complexity
The time complexity is (O(m + n)), where (m) is the length of `list1` and (n)
is the length of `list2`. The algorithm iterates through both lists, comparing their
values and linking nodes accordingly. Each node from both lists is processed 
exactly once.

### Space Complexity
The space complexity is (O(1)) in terms of additional space used because it only uses
a few pointers (`t1`, `t2`, `t3`) and does not create any new nodes other than the
merged list. However, if you consider the newly created nodes for the merged list, 
the total space used will be proportional to the total number of nodes in both lists, 
leading to an overall space complexity of \(O(m + n)\) in terms of the output list.

### Summary
- **Time Complexity:** (O(m + n))
- **Space Complexity:** (O(1)) (excluding the space for the merged list) or (O(m + n))
 (including the space for the merged list).
'''

'''
The `mergeTwoLists2` function merges two sorted linked lists recursively. 
Here’s the analysis of its time and space complexity:

### Time Complexity
The time complexity is (O(m + n)), where (m) is the length of `list1` and (n) 
is the length of `list2`. Similar to the iterative approach, each node in both lists 
is processed exactly once, resulting in a linear traversal of both lists.

### Space Complexity
The space complexity is \(O(m + n)\) due to the recursive call stack. In the worst case,
the recursion can go as deep as the total number of nodes in both lists, leading to 
additional space usage proportional to the number of nodes. Each recursive call adds a 
new frame to the call stack.

### Summary
- **Time Complexity:** (O(m + n))
- **Space Complexity:** (O(m + n)) (due to the recursion)
'''