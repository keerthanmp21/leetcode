import heapq
from typing import List


class Solution:
    # maxheap
    # tc O(m*n*logk), sc O(k)
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        maxHeap = []
        for r in range(ROWS):
            for c in range(COLS):
                heapq.heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return -heapq.heappop(maxHeap)

    # minHeap
    # tc O(k*logk), sc O(k)
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        minHeap = []  # [value, row, col]
        for r in range(min(k, ROWS)):
            heapq.heappush(minHeap, [matrix[r][0], r, 0])

        res = -1
        for i in range(k):
            res, r, c = heapq.heappop(minHeap)
            if (c + 1) < COLS:
                heapq.heappush(minHeap, [matrix[r][c + 1], r, c + 1])
        return res

    # binary search
    # tc O(log(m*n)), sc O(1)
    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def getCountLessOrEqual(val):
            cnt = 0
            c = n - 1
            for r in range(m):
                while c >= 0 and matrix[r][c] > val:
                    c -= 1
                cnt += c + 1
            return cnt

        l = matrix[0][0]
        r = matrix[-1][-1]
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if getCountLessOrEqual(mid) >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
