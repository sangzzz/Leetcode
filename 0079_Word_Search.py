class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        elif len(board[0]) == 0:
            return False
        visited = [[False for i in range(len(board[0]))]
                   for j in range(len(board))]
        global flag
        flag = False

        def dfs(visited, char_pos, i, j):
            global flag
            if char_pos == len(word):
                flag = True
                return flag
            visited[i][j] = True
            char = word[char_pos]
            if i+1 < len(board) and not visited[i+1][j] and board[i+1][j] == char:
                dfs(visited, char_pos+1, i+1, j)
                if flag:
                    return True

            if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == char:
                dfs(visited, char_pos + 1, i-1, j)
                if flag:
                    return True

            if j+1 < len(board[0]) and not visited[i][j+1] and board[i][j+1] == char:
                dfs(visited, char_pos + 1, i, j+1)
                if flag:
                    return True

            if j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == char:
                dfs(visited, char_pos + 1, i, j-1)
                if flag:
                    return True

            visited[i][j] = False
            return False

        if len(word) > len(board)*len(board[0]):
            return False
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    flag = False
                    dfs(visited, 1, i, j)
                    if flag:
                        return True
        return False
