class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        dp[(len(s), len(p))] = True

        def check(j):
            # print(dp)
            if (len(p) - j) % 2 != 0:
                return False
            for i in range(j+1, len(p), 2):
                if p[i] != '*':
                    return False
            return True

        def mtch(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(p) and i < len(s):
                return False
            elif j < len(p) and i == len(s):
                return check(j)
            elif s[i] != p[j] and p[j] != '.':
                if j == len(p)-1 or p[j+1] != '*':
                    dp[(i, j)] = False
                else:
                    dp[(i, j)] = mtch(i, j+2)
            elif s[i] == p[j] or p[j] == '.':
                if j == len(p)-1 or p[j+1] != '*':
                    dp[(i, j)] = mtch(i+1, j+1)
                else:
                    dp[(i, j)] = mtch(i+1, j) or mtch(i, j+2)
            return dp[(i, j)]
        x = mtch(0, 0)
        return x
