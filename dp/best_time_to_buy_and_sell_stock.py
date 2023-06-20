# two pointers
# tc O(n), sp O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
            r += 1
        return maxP

# brute force
# tc O(n^2), sc O(1)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxProfit = 0
        for i in range(N-1):
            for j in range(i+1, N):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit

#dp tabulation
# tc O(n), sc O(n) 
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [0]*N
        dp[N-1] = prices[N-1]

        for i in range(N-2,-1,-1):
            dp[i] = max(prices[i],dp[i+1])

        maxProfit = 0
        for i in range(N):
            maxProfit = max(maxProfit, dp[i]-prices[i])

        return maxProfit

# dp space optimization
# tc O(n), sc O(1) 
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('infinity')
        for i in range(len(prices)):
            profit = max(profit,prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return profit
        













