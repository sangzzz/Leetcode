class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        n = len(matrix)
        m = len(matrix[0])
        assert m == n

        for i in range(0, n):
            for j in range(0, n//2):
                matrix[i][j], matrix[i][-(j+1)
                                        ] = matrix[i][-(j+1)], matrix[i][j]

        for i in range(0, n-1):
            for j in range(0, n-i-1):
                matrix[i][j], matrix[n-j-1][n-i -
                                            1] = matrix[n-1-j][n-1-i], matrix[i][j]
