from typing import Optional
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