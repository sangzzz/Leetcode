class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        T = {}
        T[(1, 1)] = 0
        for i in range(1, m+1):
            T[(1, i)] = 1
        for i in range(1, n+1):
            T[(i, 1)] = 1
        for i in range(2, m+1):
            for j in range(2, n+1):
                T[(j, i)] = T[(j, i-1)] + T[(j-1, i)]
        return T[(n, m)]
