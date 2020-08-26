class Solution:
    def totalNQueens(self, n: int) -> int:
        global grid, sol, cnt
        # sol = []
        if n == 1:
            return 1
        if n <= 3:
            return 0
        grid = [['.' for i in range(0, n)] for j in range(0, n)]
        cnt = 0

        def check_columns(i, j):
            for k in range(n):
                if grid[k][j] == 'Q':
                    return False
            return True

        def check_rows(i, j):
            for k in range(n):
                if grid[i][k] == 'Q':
                    return False
            return True

        def check_diagonals(i, j):
            a = i
            b = j
            while a <= n-1 and b <= n-1:
                if grid[a][b] == 'Q':
                    return False
                a += 1
                b += 1
            a = i
            b = j
            while a >= 0 and b >= 0:
                if grid[a][b] == 'Q':
                    return False
                a -= 1
                b -= 1
            a = i
            b = j
            while a >= 0 and b <= n-1:
                if grid[a][b] == 'Q':
                    return False
                a -= 1
                b += 1
            a = i
            b = j
            while a <= n-1 and b >= 0:
                if grid[a][b] == 'Q':
                    return False
                a += 1
                b -= 1
            return True

        def check(i, j):
            return check_rows(i, j) and check_columns(i, j) and check_diagonals(i, j)

        def solve(i):
            global cnt
            if i == n:
                cnt += 1
                return True
            # print(i)
            for j in range(n):
                if check(i, j):
                    grid[i][j] = 'Q'
                    # prin/t(grid)
                    if not solve(i + 1):
                        grid[i][j] = '.'
                        continue
                    else:
                        grid[i][j] = '.'
            return False
        solve(0)
        return cnt
