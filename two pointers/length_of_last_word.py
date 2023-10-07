class Solution:
    # brute force
    # tc O(n), sc O(n)
    def lengthOfLastWord1(self, s: str) -> int:
        l = s.split(" ")
        l2 = []
        for i in l:
            if i != "":
                l2.append(i)
        return len(l2[-1])

    # two pointers
    # tc O(res), sc O(1)
    def lengthOfLastWord(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while r >= 0:
            if s[r] == " ":
                r -= 1
            else:
                break

        l = r
        while l >= 0:
            if s[l] != " ":
                l -= 1
            else:
                break

        return r - l
