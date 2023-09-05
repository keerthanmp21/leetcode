from typing import List


class Solution:
    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []
        # base case
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

    # tc O(n*n!), sc O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        N = len(nums)

        def backtrack(pos, cur):
            if pos == N:
                result.append(cur[:])  # cur.copy = cur[:]
                return
            for i in range(N):
                if i not in visited:
                    visited.add(i)
                    backtrack(pos + 1, cur + [nums[i]])
                    visited.remove(i)

        backtrack(0, [])
        return result
