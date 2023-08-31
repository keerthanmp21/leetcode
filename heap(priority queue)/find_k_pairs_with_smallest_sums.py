from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        minHeap = [[nums1[i] + nums2[0], i, 0] for i in range(len(nums1))]
        heapq.heapify(minHeap)

        res = []
        while k > 0 and minHeap:
            [_, i, j] = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(minHeap, [nums1[i] + nums2[j + 1], i, j + 1])
            k -= 1

        return res
