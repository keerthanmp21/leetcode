# heap(priority queue)
# tc O(nlogk), sc O(1)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)
        

# sorting
# tc O(nlogn), sc O(1)
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]