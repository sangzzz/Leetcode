class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            return self.myPow(x * x, n // 2) * self.myPow(x, n % 2)
