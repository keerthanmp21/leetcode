# tc O(n), sc O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {} # no of occurences in string t
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        window = {} # no of occurences b/w l and r
        res, resLen = [-1,-1], float('infinity')
        l = 0
        have, need = 0, len(countT) # have = window, need = t
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen!=float('infinity') else ''


