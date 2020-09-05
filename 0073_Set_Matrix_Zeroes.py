class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        if r == 0:
            return None
        c = len(matrix[0])
        if c == 0:
            return None

        def change_column(j):
            for i in range(r):
                matrix[i][j] = 0

        def change_row(i):
            for j in range(c):
                matrix[i][j] = 0

        rows = set()
        columns = set()
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in list(rows):
            change_row(i)
        for j in list(columns):
            change_column(j)
