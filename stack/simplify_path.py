class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')

        for p in path_list:
            if stack and p == '..':
                stack.pop()
            elif p not in ['','.','..']:
                stack.append(p)

        return '/'+ '/'.join(stack)