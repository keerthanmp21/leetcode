from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for i in arr:
            diff.append(abs(i-x))

        res = [0,k]
        curSum = sum(arr[0:k+1])
        minSum = curSum
        l = 0
        for r in range(k,len(arr)):
            curSum -= diff[l]
            l += 1
            curSum += diff[r]
            if curSum < minSum:
                res = [l,r+1]
                minSum = curSum

        return arr[res[0]:res[1]]
