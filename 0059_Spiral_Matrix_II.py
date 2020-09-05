class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]
        visited = [[False for i in range(n)] for j in range(n)]
        i = 0
        j = 0
        inc = ('col', 1)
        moves_exist = True
        cnt = 1
        while moves_exist:
            if inc[0] == 'col':
                if not visited[i][j]:
                    visited[i][j] = cnt
                    cnt += 1
                j += inc[1]
                if (j < 0 or j >= n) or visited[i][j]:
                    j -= inc[1]
                    inc = ('row', inc[1])
                    if visited[i+inc[1]][j]:
                        moves_exist = False

            else:
                if not visited[i][j]:
                    visited[i][j] = cnt
                    cnt += 1
                i += inc[1]
                if i < 0 or i >= n or visited[i][j]:
                    i -= inc[1]
                    inc = ('col', -inc[1])
                    if visited[i][j+inc[1]]:
                        moves_exist = False
        return visited
