class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in T[('r', i)] and board[i][j] not in T[('c', j)]:
                    T[('r', i)].append(board[i][j])
                    T[('c', j)].append(board[i][j])
                else:
                    return False
                if board[i][j] not in T[(i//3, j//3)]:
                    T[(i//3, j//3)].append(board[i][j])
                else:
                    return False
        # print(T)
        return True
