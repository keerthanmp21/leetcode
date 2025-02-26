# tc O(logn), sc O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if x < mid * mid: # check whether sqrt comes b/w l and mid
                r = mid-1
            elif x > (mid + 1) * (mid + 1):# check whether sqrt comes b/w mid and r
                l = mid + 1
            elif mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            else:
                return mid + 1
            
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if x < mid * mid:
                r = mid - 1
            elif x > mid * mid:
                l = mid + 1
            else:
                return mid

        return r