from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # outer bound
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if target >= letters[mid]:
                l = mid + 1
            elif target < letters[mid]:
                r = mid - 1
        return letters[l]
