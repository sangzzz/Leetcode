class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        # if m==0:
        #     return 0
        n = len(obstacleGrid[0])
        # if n==0:
        #     return 0
        if obstacleGrid == [[0]] or obstacleGrid == [[]]:
            return 1
        T = [[0 for i in range(0, n)] for j in range(0, m)]
        T[0][0] = 0
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            T[i][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                break
            T[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    T[i][j] = 0
                else:
                    T[i][j] = T[i-1][j] + T[i][j-1]
        print(T)
        return T[-1][-1]
