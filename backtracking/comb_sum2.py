from typing import List

class Solution:
    # tc O(2^n), sc O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        candidateLen = len(candidates)
        def backtrack(pos, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return 
            prev = -1
            for i in range(pos,candidateLen):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, total+candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack(0, [], 0)
        return res