from typing import List

class Solution:
    # brute force O(m*n)
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        COLS, ROWS = len(matrix[0]), len(matrix)
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == target:
                    return True
        return False

    # binary search O(m*log(n))
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                # mid = (l+r)//2
                mid = l + ((r - l) // 2)
                if target > matrix[row][mid]:
                    l = mid + 1
                elif target < matrix[row][mid]:
                    r = mid - 1
                else:
                    return True
        return False
