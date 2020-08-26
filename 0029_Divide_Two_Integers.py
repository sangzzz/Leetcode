class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1 or divisor == -1:
            if (dividend//divisor) >= 2**31:
                return (2**31 - 1)
            if (dividend//divisor) < (-(2**31)):
                return (-(2**31))
            return dividend//divisor
        n1 = 1
        n2 = 1
        if dividend < 0:
            n1 = -1
            dividend = -dividend
        if divisor < 0:
            n2 = -1
            divisor = -divisor
        flag = n1*n2
        return (dividend//divisor)*flag
