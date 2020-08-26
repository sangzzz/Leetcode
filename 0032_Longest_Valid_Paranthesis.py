class Solution:
    def longestValidParentheses(self, s: str) -> int:
        T = {}
        stack = []
        for j in range(len(s)):
            if s[j] == '(':
                stack.append(j)
                T[j] = 0
            else:
                if len(stack) > 0:
                    T[stack[-1]] = 1
                    stack = stack[0:-1]
                else:
                    T[j] = -1
        mcnt = 0
        cnt = 0
        for i in T:
            if T[i] == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt > mcnt:
                mcnt = cnt
        return mcnt*2
