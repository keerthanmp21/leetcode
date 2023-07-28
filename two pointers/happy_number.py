class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit: # iterate until cycle detect or n becomes 1(return)
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n%10
            digit = digit**2
            output += digit
            n = n//10
        return output

class Solution2:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            if slow == fast:
                break
        return slow==1

    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n%10
            digit = digit**2
            output += digit
            n = n//10
        return output