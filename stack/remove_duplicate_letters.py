class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}

        for i in range(len(s)):
            last_index[s[i]] = i

        stack = []
        visited = set()

        for i in range(len(s)):
            if s[i] not in visited:
                # monotonic increasing stack
                while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)
