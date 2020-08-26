class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        dp[(len(s), len(p))] = True

        def check(j):
            for i in p[j:]:
                if i != '*':
                    return False
            return True

        def mtch(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            elif i == len(s) and j == len(p):
                return False
            elif i == len(s) and j < len(p):
                return check(j)
            elif i < len(s) and j == len(p):
                return False
            elif s[i] != p[j] and p[j] != '?':
                if p[j] == '*':
                    dp[(i, j)] = mtch(i+1, j) or mtch(i, j+1)
                else:
                    dp[(i, j)] = False
            elif s[i] == p[j] or p[j] == '?':
                dp[(i, j)] = mtch(i+1, j+1)
            return dp[(i, j)]
        x = mtch(0, 0)
        # print(dp)
        return x
