from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def dfs(i, subset):
            if i > 10:
                return
            if len(subset) == k:
                if sum(subset) == n:
                    return result.append(subset.copy())
                else:
                    return

            subset.append(i)
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(1, [])

        return result
