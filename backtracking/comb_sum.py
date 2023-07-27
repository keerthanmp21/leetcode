from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidatesLen = len(candidates)
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=candidatesLen or total>target:
                return
            # include
            cur.append(candidates[i])
            backtrack(i,cur,total+candidates[i])
            # not include
            cur.pop()
            backtrack(i+1,cur,total)
        backtrack(0,[],0)
        return res