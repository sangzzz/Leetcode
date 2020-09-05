class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        start = 1
        end = 2
        while start <= x//2:
            if end*end > x:
                break
            else:
                start = end
                end *= 2
        for i in range(start+1, end+1):
            if i*i <= x:
                start = i
            else:
                break
        return start
