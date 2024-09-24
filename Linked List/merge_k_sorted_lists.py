from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        cnt = 0

        for listnode in lists:
            while listnode:
                heapq.heappush(minHeap, (listnode.val, cnt, listnode))
                listnode = listnode.next
                cnt += 1

        res = ListNode(0)
        t1 = res
        while minHeap:
            _, _, listnode = heapq.heappop(minHeap)
            t1.next = listnode
            t1 = t1.next

        return res.next
    
'''
The `mergeKLists` function merges (k) sorted linked lists into a single sorted linked 
list using a min-heap (priority queue). Here’s the analysis of its time and space 
complexity:

### Time Complexity
The time complexity is (O(Nlogk)), where (N) is the total number of nodes across all (k) lists. This is because:
1. In the first loop, we iterate through each of the (k) linked lists and push each 
node into the min-heap, which takes (O(log k)) time for each insertion.
2. In the second loop, we pop each node from the min-heap (which takes (O(log k)) 
for each pop) and link them together, which also takes (O(N)) in total for (N) nodes.

### Space Complexity
The space complexity is (O(k)) for the min-heap, as it stores at most (k) nodes at any
 given time (one from each list). Additionally, the output linked list does not count 
 towards the space complexity since it is the final result.

### Summary
- **Time Complexity:** (O(Nlogk))
- **Space Complexity:** (O(k))
'''
