class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        T = {'(': ')', '[': ']', '{': '}'}
        o = ['(', '[', '{']
        c = ['}', ']', ')']
        for i in s:
            if i in o:
                stack.append(i)
            elif i in c:
                try:
                    if T[stack[-1]] == i:
                        stack = stack[0:-1]
                    else:
                        return False
                except:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
