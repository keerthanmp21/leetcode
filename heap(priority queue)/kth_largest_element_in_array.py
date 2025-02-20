from typing import List
import heapq


class Solution:
    # heap(priority queue)
    # tc O(nlogk), sc O(1)
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)

    # sorting
    # tc O(nlogn), sc O(1)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        return heapq.nlargest(k, minHeap)[-1]