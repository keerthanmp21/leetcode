class Solution:

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # validate(a prefix + b suffix) and validate(b suffix + a prefix)
        return self.validate(a, b) or self.validate(b, a)

    def validate(self, s1, s2):
        print("=====", s1, s2)
        l = 0
        r = len(s1) - 1

        while l < r:
            if s1[l] != s2[r]:
                break
            l += 1
            r -= 1

        if l >= r:
            return True
        return self.isPali(s1, l, r) or self.isPali(s2, l, r)

    def isPali(self, s, l, r):
        print("-----", s, l , r)
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
        
        
s = Solution()
#print(s.checkPalindromeFormation("abdef", "fecab"))
#print(s.checkPalindromeFormation("ulacfd", "jizalu"))
print(s.checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"))



