class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        T = [[0 for i in range(0, c)] for j in range(0, r)]
        T[0][0] = grid[0][0]
        for i in range(1, r):
            T[i][0] = T[i-1][0]+grid[i][0]
        for i in range(1, c):
            T[0][i] = T[0][i-1]+grid[0][i]
        for i in range(1, r):
            for j in range(1, c):
                T[i][j] = min(T[i-1][j], T[i][j-1]) + grid[i][j]
        # print(T)
        return T[-1][-1]
