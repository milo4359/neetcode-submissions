class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[m][0] > target:
                r = m - 1
            elif m + 1 == len(matrix) or (matrix[m][0] <= target and matrix[m + 1][0] > target):
                row = m
                break
            else:
                l = m + 1

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else: return True
        return False
