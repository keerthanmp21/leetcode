# backtrack
# tc O(2^n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        N = len(s)

        def backtrack(start):
            if start == N:
                return True
            for end in range(start+1,N+1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    return True
            return False
        return backtrack(0)
        
# dp
# tc O(n^2), sc O(n)
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        N = len(s)
        dp = [-1]*N
        def backtrack(start):
            if start == N:
                return True
            if dp[start] != -1:
                return dp[start]
            for end in range(start+1,N+1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    dp[start] = 1
                    return dp[start]
            dp[start] = 0
            return dp[start]
        return backtrack(0)
        
class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        #same as above but using inbuilt decorator
        wordDictSet = set(wordDict)
        N = len(s)
        @lru_cache(None)
        def backtrack(start):
            if start == N:
                return True
            for end in range(start+1,N+1):
                word = s[start:end]
                if word in wordDictSet and backtrack(end):
                    return True
            return False
        return backtrack(0)

# dp tabulation
# tc O(n^2), sc O(n)
class Solution4:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
                    
        return dp[0]
        