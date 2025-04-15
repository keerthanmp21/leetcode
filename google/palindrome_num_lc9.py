class Solution:
    # time complexity O(n)
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False

        res = []
        while x > 0:
            res.append(x % 10)
            x = x // 10

        n = len(res)
        l, r = 0, n - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1

        return True

    # time complexity O(logN)
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False

        res = 0
        y = x
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10

        return res == y
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        return x == reversed_half or x == reversed_half // 10
        