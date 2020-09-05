class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False
        elif target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        low = 0
        high = len(matrix) - 1
        m = low + (high-low)//2
        while True:
            m = low + (high-low)//2
            try:
                if matrix[m][0] <= target < matrix[m+1][0]:
                    break
                elif matrix[m][0] > target:
                    high = m - 1
                else:
                    low = m + 1
            except:
                break
        low = 0
        high = len(matrix[m]) - 1
        try:
            x = matrix[m].index(target)
            return True
        except:
            return False
