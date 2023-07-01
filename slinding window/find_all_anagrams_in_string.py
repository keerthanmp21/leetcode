# tc O(n), sc O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenP = len(p)
        lenS = len(s)
        if lenP>lenS:
            return []
        pCount = {}
        sCount = {}
        for i in range(lenP):
            pCount[p[i]] = pCount.get(p[i],0)+1
            sCount[s[i]] = sCount.get(s[i],0)+1

        l = 0
        res = [0] if pCount == sCount else []

        for r in range(lenP,lenS):
            sCount[s[r]] = sCount.get(s[r],0)+1
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                #sCount.pop(s[l])
                del sCount[s[l]]
            l += 1
            if sCount == pCount:
                res.append(l)

        return res   