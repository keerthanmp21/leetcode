import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        N = len(nums)
        maxHeap = []
        for i in range(k): # first window of k size
            heapq.heappush(maxHeap, (-nums[i],i))
        res = [-maxHeap[0][0]] # add max value of first window
        for i in range(k,N): # start from second window
            while maxHeap[0][1] <= i-k: # outer bound
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[i],i))
            res.append(-maxHeap[0][0])
        return res