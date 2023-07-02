# tc O(logn), sc O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if x < mid * mid:
                r = mid-1
            elif x > (mid + 1) * (mid + 1):
                l = mid + 1
            elif mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            else:
                return mid + 1