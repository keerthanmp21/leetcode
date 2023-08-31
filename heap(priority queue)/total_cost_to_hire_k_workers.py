import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i, j = 0, len(costs)-1
        first_candidates = []
        last_candidates = []
        res = 0
        while k > 0:
            while len(first_candidates) < candidates and i <= j:
                heapq.heappush(first_candidates, costs[i])
                i += 1
            while len(last_candidates) < candidates and i <= j:
                heapq.heappush(last_candidates, costs[j])
                j -= 1
            
            first_value = first_candidates[0] if first_candidates else float('infinity')
            last_value = last_candidates[0] if last_candidates else float('infinity')

            if first_value <= last_value:
                res += first_value
                heapq.heappop(first_candidates)
            else:
                res += last_value
                heapq.heappop(last_candidates)
            k -= 1
        return res