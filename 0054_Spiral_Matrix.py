class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1:
            return []
        if len(matrix) == 1:
            return matrix[0]
        r = len(matrix)
        c = len(matrix[0])
        visited = [[False for i in range(c)] for j in range(r)]
        i = 0
        j = 0
        inc = ('col', 1)
        moves_exist = True
        res = []
        while moves_exist:
            if inc[0] == 'col':
                if not visited[i][j]:
                    res.append(matrix[i][j])
                visited[i][j] = True
                j += inc[1]
                if (j < 0 or j >= c) or visited[i][j]:
                    j -= inc[1]
                    inc = ('row', inc[1])
                    if visited[i+inc[1]][j]:
                        moves_exist = False

            else:
                if not visited[i][j]:
                    res.append(matrix[i][j])
                visited[i][j] = True
                i += inc[1]
                if i < 0 or i >= r or visited[i][j]:
                    i -= inc[1]
                    inc = ('col', -inc[1])
                    if visited[i][j+inc[1]]:
                        moves_exist = False
        print(res)
        return res
