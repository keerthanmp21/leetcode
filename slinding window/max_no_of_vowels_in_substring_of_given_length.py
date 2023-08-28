# sliding window
# tc O(n), sc O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        numOfVowels = 0
        res = 0
        for r in range(len(s)):
            if s[r] in "aeiou":
                numOfVowels += 1
            if (r - l + 1) == k:
                res = max(res, numOfVowels)
                if s[l] in "aeiou":
                    numOfVowels -= 1
                l += 1
        return res
