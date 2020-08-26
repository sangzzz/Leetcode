class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        T = {}
        for i in range(0, 9):
            T[('r', i)] = []
            T[('c', i)] = []
        T[(0, 0)] = []
        T[(1, 0)] = []
        T[(2, 0)] = []
        T[(0, 1)] = []
        T[(1, 1)] = []
        T[(2, 1)] = []
        T[(0, 2)] = []
        T[(1, 2)] = []
        T[(2, 2)] = []
        flag = True
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                board[i][j] = int(board[i][j])
                if board[i][j] not in T[('r', i)] and board[i][j] not in T[('c', j)]:
                    T[('r', i)].append(board[i][j])
                    T[('c', j)].append(board[i][j])
                else:
                    flag = False
                if board[i][j] not in T[(i//3, j//3)]:
                    T[(i//3, j//3)].append(board[i][j])
                else:
                    flag = False
        # print(T)

        def used_in_row(n, i, j):
            if n in T[('r', i)]:
                return True
            return False

        def used_in_col(n, i, j):
            if n in T[('c', j)]:
                return True
            return False

        def used_in_box(n, i, j):
            if n in T[(i//3, j//3)]:
                return True
            return False

        def safe(n, i, j):
            return not used_in_col(n, i, j) and not used_in_row(n, i, j) and not used_in_box(n, i, j)

        def add(n, i, j):
            T[('r', i)].append(n)
            T[('c', j)].append(n)
            T[(i//3, j//3)].append(n)
            board[i][j] = n

        def remove(n, i, j):
            T[('r', i)].remove(n)
            T[('c', j)].remove(n)
            T[(i//3, j//3)].remove(n)
            board[i][j] = '.'

        def find_empty_location():
            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == '.':
                        return [i, j]
            return [-1, -1]

        def solve_sudoku():
            l = find_empty_location()
            if l == [-1, -1]:
                return True

            i = l[0]
            j = l[1]

            for n in range(1, 10):
                if safe(n, i, j):
                    add(n, i, j)
                    if solve_sudoku():
                        return True
                    remove(n, i, j)
            return False

        solve_sudoku()
        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = str(board[i][j])
