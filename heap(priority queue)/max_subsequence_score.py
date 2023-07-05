import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        minHeap = []
        res = 0
        total = 0

        for a,b in sorted(list(zip(nums1, nums2)), key=lambda value:-value[1]):
            total += a
            heapq.heappush(minHeap, a)
            if len(minHeap) > k:
                total -= heapq.heappop(minHeap)
            if len(minHeap) == k:
                res = max(res, total*b)

        return res