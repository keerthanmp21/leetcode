class Solution:
    # two pointers
    # tc O(n^2), sc O(1)
    def longestPalindrome(self, s: str) -> str:
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
    
    # brute force
    # tc O(n^3), sp O(1)    
    def longestPalindrome2(self, s: str) -> str:
        N = len(s)
        startingIndex = 0
        maxLen = 0

        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPali(i,j):
                    if (j-i+1) > maxLen:
                        maxLen = (j-i+1)
                        startingIndex = i

        return s[startingIndex:startingIndex+maxLen]

    # dp tabulation (bottom up) iterative
    # tc O(n^2), sc O(n^2)
    def longestPalindrome3(self, s: str) -> str:
        sLen = len(s)
        dp = [[False]*sLen for _ in range(sLen)]
        #filling out the diagonal by 1
        for i in range(sLen):
            dp[i][i] = True
        longest_palindrome = s[-1]

        # filling the dp table
        for i in range(sLen-1,-1,-1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i+1,sLen):
                if s[i] == s[j]:#if the chars matches
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(s[i:j+1]) > len(longest_palindrome):
                            longest_palindrome = s[i:j+1]

        return longest_palindrome