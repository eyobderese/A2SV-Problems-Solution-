class Solution:
    def simplifyPath(self, path: str) -> str:
        m = path.split('/')

        stack = []

        for i in m:
            if i and i != '..' and i != '.':
                stack.append(i)
            elif i == '..' and stack:
                stack.pop()

        n = '/'.join(stack)
        n = '/' + n

        return n
