from typing import List

# tc O(log(m+n)), sc O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # find row in which target is in.
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False