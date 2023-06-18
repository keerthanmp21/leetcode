class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
                
            # even length
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
                
        return res
    

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        # dp tabulation (bottom up) iterative
        sLen = len(s)
        dp = [[False]*sLen for _ in range(sLen)]
        for i in range(sLen):
            dp[i][i] = True
        longest_palindrome = s[-1]

        for i in range(sLen-1,-1,-1):
            for j in range(i+1,sLen):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        if len(s[i:j+1]) > len(longest_palindrome):
                            longest_palindrome = s[i:j+1]

        return longest_palindrome






