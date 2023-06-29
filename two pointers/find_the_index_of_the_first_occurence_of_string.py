# brute force
# tc O(m*n), sc O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

# two pointers
# tc O(m), sc O(1) 
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2, r1, r2 = 0, 0, len(haystack), len(needle)
        while l1<r1:
            if l2 == r2:
                return l1-l2
            if haystack[l1] == needle[l2]:
                l2 += 1
            else:
                l1 = l1-l2
                l2 = 0
            l1 += 1
        if l2==r2:
            return l1-l2
        return -1