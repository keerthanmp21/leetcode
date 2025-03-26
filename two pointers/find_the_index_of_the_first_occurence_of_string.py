class Solution:
    # brute force
    # tc O(m*n), sc O(1)
    def strStr1(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

    # two pointers
    # tc O(m), sc O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2, r1, r2 = 0, 0, len(haystack), len(needle)
        while l1 < r1:
            if l2 == r2:
                return l1 - l2
            if haystack[l1] == needle[l2]:
                l2 += 1
            else:
                l1 = l1 - l2
                l2 = 0
            l1 += 1
        if l2 == r2:
            return l1 - l2
        return -1

    def strStr3(self, haystack: str, needle: str) -> int:
        def compute_lps(pattern):
            """Computes the LPS (Longest Prefix Suffix) array."""
            m = len(pattern)
            lps = [0] * m
            j = 0  # Length of previous longest prefix suffix

            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            return lps

        def kmp_search(text, pattern):
            """Searches for occurrences of 'pattern' in 'text' using KMP algorithm."""
            n, m = len(text), len(pattern)
            lps = compute_lps(pattern)

            j = 0  # Pointer for pattern
            occurrences = []

            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]

                if text[i] == pattern[j]:
                    j += 1
                
                if j == m:
                    return (i - m + 1)
                    

            return -1

        res = kmp_search(haystack, needle)
        return res