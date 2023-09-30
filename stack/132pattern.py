from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # i and k val can be stored in stack as it is monotonic
        j_val = float("-inf")

        for i in reversed(nums):
            if i < j_val:
                return True
            # monotonic decreasing
            # not monotonic inc coz when we pop we need max value to be stored in j_val
            while stack and i > stack[-1]:
                j_val = stack.pop()
            stack.append(i)

        return False
