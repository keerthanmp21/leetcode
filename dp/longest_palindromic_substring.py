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
    
# brute force
# tc O(n^3), sp O(1)    
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        maxLen = 0
        starting_index = 0
        def isPali(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for l in range(0,N):
            for r in range(l,N):
                if isPali(l,r):
                    if (r-l+1)>maxLen:
                        maxLen = r-l+1
                        starting_index = l
        return s[starting_index:starting_index+maxLen]

# dp tabulation (bottom up) iterative
# tc O(n^2), sc O(n^2)
class Solution3:
    def longestPalindrome(self, s: str) -> str:
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






