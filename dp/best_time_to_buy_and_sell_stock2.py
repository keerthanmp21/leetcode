# backtrack
# tc O(2^n), sc O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        def backtrack(idx, canBuy):
            if idx == N:
                return 0
            res = backtrack(idx+1, canBuy) #skip
            if canBuy:
                res = max(res, backtrack(idx+1,False)-prices[idx]) #buy
            else:
                res = max(res, backtrack(idx+1,True)+prices[idx]) #sell
            return res
        return backtrack(0,True)
        
#dp memoization
# tc O(n), sc O(n)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}
        def backtrack(idx, canBuy):
            if idx == N:
                return 0
            if (idx,canBuy) in dp:
                return dp[(idx,canBuy)]
            res = backtrack(idx+1, canBuy) #skip
            if canBuy:
                res = max(res, backtrack(idx+1,False)-prices[idx]) #buy
            else:
                res = max(res, backtrack(idx+1,True)+prices[idx]) #sell
            dp[(idx,canBuy)] = res
            return dp[(idx,canBuy)]
        return backtrack(0,True)
        
# dp memoization (inbuilt cache)
# tc O(n), sc O(n)
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        @cache # or @lru_cache(None) 
        def backtrack(idx, canBuy):
            if idx == N:
                return 0
            res = backtrack(idx+1, canBuy) #skip
            if canBuy:
                res = max(res, backtrack(idx+1,False)-prices[idx]) #buy
            else:
                res = max(res, backtrack(idx+1,True)+prices[idx]) #sell
            return res
        return backtrack(0,True)
        
# greedy
# tc O(n), sc O(1)
class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                maxProfit += prices[i+1] - prices[i]
        return maxProfit