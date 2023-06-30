# two pointers
# tc O(n), sc O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1<len(s) and p2<len(t):
            p1 += (s[p1]==t[p2])
            p2 += 1
        return p1==len(s)