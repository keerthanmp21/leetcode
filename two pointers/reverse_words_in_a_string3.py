class Solution:
    # brute force
    # tc O(n*m) n = total length, m = no of words split space
    # sc O(n)
    def reverseWords1(self, s: str) -> str:
        res = ""

        for word in s.split(" "):
            res += word[::-1]
            res += " "
        res = res[:-1]
        return res

    # two pointers
    # tc same as brute force, sc O(n) coz list(s)
    def reverseWords(self, s: str) -> str:
        N = len(s)
        s = list(s)
        l = r = 0

        for i in range(N):
            if s[i] == " " or i == N - 1:
                r = i
                if i == N - 1 and s[i] != " ":
                    r += 1
                while l < r:
                    s[l], s[r - 1] = s[r - 1], s[l]
                    l += 1
                    r -= 1
                l = i + 1

        return "".join(s)
