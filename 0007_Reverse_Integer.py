class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = 0
            x = -x
        X = str(x)
        X = X[::-1]
        x = int(X)
        if flag == 0:
            x = -x
        if x not in range(-(2**31), (2**31)):
            return 0
        return x
