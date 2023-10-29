class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            print(stack)
            if i == '(':
                stack.append(count)
                count = 0

            else:
                m = stack.pop()
                count = m+max(1, count*2)

        return count
