from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        subset = ""

        def dfs(i, subset):
            while i < len(s) and (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                subset += s[i]
                i += 1
            if i >= len(s):
                return res.append(subset)

            org_alp = s[i]
            if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                conv_alp = chr(ord(s[i]) - 32)
            else:
                conv_alp = chr(ord(s[i]) + 32)

            subset += conv_alp
            dfs(i + 1, subset)

            subset = subset[:-1] + org_alp
            dfs(i + 1, subset)

        dfs(0, "")
        return res
