import heapq
from typing import List
import collections

class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
                
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N == 0 or k == 1:
            return nums
        maxHeap = []
        for i in range(k): # first window of k size
            heapq.heappush(maxHeap, [-nums[i], i])
        
        res = []
        res.append(-maxHeap[0][0]) # add max value of first window

        for i in range(k, N): # start from second window
            while maxHeap[0][1] <= i - k: # outer bound
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, [-nums[i], i])
            res.append(-maxHeap[0][0])

        return res
        